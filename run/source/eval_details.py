import datetime
from multiprocessing import Pool, cpu_count
from pathlib import Path

import cv2
from show_ref_results.utils import print_table
from source.results import Average, MultiAverage, Results
from tqdm import tqdm


def timestamp_to_filename() -> str:
    now = datetime.datetime.now()

    # format it as YYYYMMDD_HHMMSS
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    return timestamp


def do_exists(gt: Path, pred: Path) -> bool:
    if not gt.exists():
        raise FileNotFoundError(f"Ground truth directory does not exist: {gt}")
    if not pred.exists():
        raise FileNotFoundError(f"Prediction directory does not exist: {pred}")
    return True


def eval_single_dir_for_pool(args) -> dict:
    """
    Wrapper function for multiprocessing that returns results as a dictionary
    instead of modifying an Average object in-place.
    """
    ground_truth_dir, prediction_dir = args

    do_exists(gt=ground_truth_dir, pred=prediction_dir)

    results = Results(subset=ground_truth_dir.parent.name)

    gt_name_list = sorted(list(prediction_dir.glob("*.*")))

    for gt_name in tqdm(
        gt_name_list,
        total=len(gt_name_list),
        desc=ground_truth_dir.parent.name,
    ):
        gt_path = ground_truth_dir / gt_name.name
        pred_path = prediction_dir / gt_name.name

        gt = cv2.imread(gt_path.as_posix(), cv2.IMREAD_GRAYSCALE)
        # handle red masks
        gt[gt > 0] = 255
        pred = cv2.imread(pred_path.as_posix(), cv2.IMREAD_GRAYSCALE)

        results.step(pred=pred, gt=gt)

    # Return the results as a dictionary instead of adding to Average
    return {
        "subset": results.subset,
        "maxFm": results.FM.get_results()["fm"]["curve"].max(),
        "wfm": results.WFM.get_results()["wfm"],
        "mae": results.MAE.get_results()["mae"],
        "sm": results.SM.get_results()["sm"],
        "meanEm": results.EM.get_results()["em"]["curve"].mean(),
    }


def eval_multiple_dirs(
    data_dirs: list[Path],
    pred_root: Path,
    timestamp: str,
    subset_name="summary",
    gt_dir_name="gt",
) -> Average:

    if subset_name != "summary":
        subset_name = f"detailed_{subset_name}"

    # multiple dir, which belongs to same subset
    average_results = Average(file_name=f"{timestamp}_{subset_name}")

    # Prepare arguments for multiprocessing
    args_list = [
        (data_dir / gt_dir_name, pred_root / data_dir.name)
        for data_dir in data_dirs
    ]

    with Pool(processes=min(len(args_list), cpu_count())) as pool:
        results_list = pool.map(eval_single_dir_for_pool, args_list)

    # Add all results to the average
    for result in results_list:
        average_results.add(
            subset=result["subset"],
            maxFm=result["maxFm"],
            wfm=result["wfm"],
            mae=result["mae"],
            sm=result["sm"],
            meanEm=result["meanEm"],
        )

    average_results.calc()
    print_table(csv_path=average_results.csv_path)
    return average_results


def eval_multiple_subsets(
    data_dirs: dict[str, list[Path]], pred_root: Path, gt_dir_name: str
):
    # data_dirs:
    # subset_name: [Path(dir1), Path(dir2), Path(dir3)]
    timestamp = timestamp_to_filename()

    multi_average = {}
    for subset_name, paths in data_dirs.items():
        multi_average[subset_name] = eval_multiple_dirs(
            data_dirs=paths,
            pred_root=pred_root,
            timestamp=timestamp,
            subset_name=subset_name,
            gt_dir_name=gt_dir_name,
        )

    ma = MultiAverage(
        multi_average=multi_average, file_name=f"{timestamp}_summary"
    )
