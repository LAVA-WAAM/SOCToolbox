import argparse
from pathlib import Path

from source.eval_details import eval_multiple_subsets


def eval_LAVA_WAAM(data_root: Path, pred_root: Path) -> None:
    data_dirs = {
        "S-1": [
            data_root / "E2_S3_W1/E2_S3_W1_L1",
            data_root / "E2_S3_W1/E2_S3_W1_L2",
            data_root / "E2_S3_W1/E2_S3_W1_L3",
            data_root / "E2_S3_W1/E2_S3_W1_L4",
            data_root / "E2_S3_W1/E2_S3_W1_L5",
            data_root / "E2_S3_W1/E2_S3_W1_L9",
            data_root / "E2_S3_W1/E2_S3_W1_L13",
            data_root / "E2_S3_W1/E2_S3_W1_L15",
        ],
        "S-2": [
            data_root / "E3_S5_C2/E3_S5_C2_P0",
            data_root / "E3_S5_C2/E3_S5_C2_P1",
            data_root / "E3_S5_C2/E3_S5_C2_P2",
            data_root / "E3_S5_C2/E3_S5_C2_P3",
            data_root / "E3_S5_C2/E3_S5_C2_P4",
            data_root / "E3_S5_C2/E3_S5_C2_P5",
            data_root / "E3_S5_C2/E3_S5_C2_P6",
            data_root / "E3_S5_C2/E3_S5_C2_P7",
            data_root / "E3_S5_C2/E3_S5_C2_P8",
        ],
        "S-3": [
            data_root / "E5_S8_C0/E5_S8_C0_P1",
            data_root / "E5_S8_C0/E5_S8_C0_P5",
            data_root / "E5_S8_C0/E5_S8_C0_P6",
        ],
        "S-4": [
            data_root / "E5_S9_C1/E5_S9_C1_P2",
            data_root / "E5_S9_C1/E5_S9_C1_P3",
            data_root / "E5_S9_C1/E5_S9_C1_P4",
            data_root / "E5_S9_C1/E5_S9_C1_P7",
            data_root / "E5_S9_C1/E5_S9_C1_P10",
            data_root / "E5_S9_C1/E5_S9_C1_P13",
            data_root / "E5_S9_C1/E5_S9_C1_P14",
            data_root / "E5_S9_C1/E5_S9_C1_P16",
            data_root / "E5_S9_C1/E5_S9_C1_P19",
            data_root / "E5_S9_C1/E5_S9_C1_P25",
        ],
        "S-5": [
            data_root / "E6_S13_C1/E6_S13_C1_V1_9",
            data_root / "E6_S13_C1/E6_S13_C1_V1_10",
        ],
    }

    eval_multiple_subsets(
        data_dirs=data_dirs, pred_root=pred_root, gt_dir_name="masks"
    )


if __name__ == "__main__":
    # ADAPT PATHS

    # LAVA_WAAM - pretrained isnet_pth:
    data_dir = "/home/docker/isnet_datasets/LAVA_WAAM/"
    pred_dir = "/home/docker/inference_results_isnet/LAVA_WAAM_isnet_pth/"

    # LAVA_WAAM - fine-tuned_pth:
    # data_dir = "/home/docker/isnet_datasets/LAVA_WAAM/"
    # pred_dir = "/home/docker/inference_results_isnet/LAVA_WAAM_fine-tuned_pth/"

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_dir", default=data_dir, help="Path to the dataset directory."
    )
    parser.add_argument(
        "--pred_dir",
        default=pred_dir,
        help="Path to the predictions directory.",
    )
    args = parser.parse_args()
    eval_LAVA_WAAM(
        data_root=Path(args.data_dir),
        pred_root=Path(args.pred_dir),
    )
