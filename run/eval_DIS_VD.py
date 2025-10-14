import argparse
from pathlib import Path

from source.eval_details import eval_multiple_dirs, timestamp_to_filename


def eval_DIS_VD(data_root: Path, pred_root: Path) -> None:
    data_dirs: list[Path] = [
        data_root / "DIS-VD",
    ]
    eval_multiple_dirs(
        data_dirs=data_dirs,
        pred_root=pred_root,
        timestamp=timestamp_to_filename(),
    )


if __name__ == "__main__":
    # ADAPT PATHS
    data_dir = "/home/docker/isnet_datasets/DIS5K/"
    pred_dir = "/home/docker/inference_results_isnet/DIS5K_isnet_pth/"

    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", default=data_dir)
    parser.add_argument(
        "--pred_dir",
        default=pred_dir,
    )
    args = parser.parse_args()

    eval_DIS_VD(
        data_root=Path(args.data_dir),
        pred_root=Path(args.pred_dir),
    )
