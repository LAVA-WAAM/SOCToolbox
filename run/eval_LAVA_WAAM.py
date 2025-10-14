import argparse
from pathlib import Path

from source.eval_details import eval_multiple_subsets


def eval_LAVA_WAAM(data_root: Path, pred_root: Path) -> None:
    data_dirs = {
        "S-1": [
            # oxidation
            data_root / "E3_S4_C1/E3_S4_C1_P2_6",
            data_root / "E5_S7_C0/E5_S7_C0_P13",
            data_root / "E5_S7_C0/E5_S7_C0_P14",
            data_root / "E5_S8_C0/E5_S8_C0_P1",
            data_root / "E5_S10_C0/E5_S10_C0_P8",
        ],
        "S-2": [
            data_root / "E3_S5_C2/E3_S5_C2_P0",
            data_root / "E3_S5_C2/E3_S5_C2_P5",
            data_root / "E4_S6_C0/E4_S6_C0_P2_12",
            data_root / "E4_S6_C0/E4_S6_C0_P3",
        ],
        "S-3": [
            data_root / "E5_S9_C1/E5_S9_C1_P7",
            data_root / "E5_S9_C1/E5_S9_C1_P16",
            data_root / "E5_S9_C1/E5_S9_C1_P19",
            data_root / "E5_S11_C2/E5_S11_C2_P5",
            data_root / "E5_S11_C2/E5_S11_C2_P10_1",
            data_root / "E5_S11_C2/E5_S11_C2_P11",
        ],
        "S-4": [
            data_root / "E6_S12_T1/E6_S12_T1_A1_4",
            data_root / "E6_S12_T1/E6_S12_T1_A1_6",
            data_root / "E6_S12_T1/E6_S12_T1_B2_3",
            data_root / "E6_S12_T1/E6_S12_T1_B2_5",
        ],
        "S-5": [
            data_root / "E6_S14_C2/E6_S14_C2_V4",
            data_root / "E6_S14_C2/E6_S14_C2_V6_3",
            data_root / "E6_S14_C2/E6_S14_C2_V7_1",
            data_root / "E6_S15_C3/E6_S15_C3_V2_0",
            data_root / "E6_S15_C3/E6_S15_C3_V2_1",
            data_root / "E6_S15_C3/E6_S15_C3_V2_6",
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
    # gt_dir = "/home/docker/isnet_datasets/LAVA_WAAM/"
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
