# _Efficient SOC Toolbox_ & _LAVA-WAAM_
## 1. Description

This repository is a fork of the [Efficient SOC Toolbox](https://github.com/mczhuge/SOCToolbox) and is provided as complementary material for the **LAVA-WAAM dataset**.

It is designed to be used together with the pretrained and fine-tuned [DIS IS-Net](https://github.com/xuebinqin/DIS) models.

The following scripts compute quantitative results for inference masks generated in “valid” mode using `IS-Net` (see the [II. Inference for datasets without ground truth](https://github.com/xuebinqin/DIS?tab=readme-ov-file#ii-inference-for-dataset-withwithout-ground-truth) section).


## 2. Setup
```bash
# clone the repository
git clone https://github.com/LAVA-WAAM/SOCToolbox.git
cd SOCToolbox

# create new env
conda create -n soc_env python=3.11
conda activate soc_env

# install dependencies
pip install -r requirements.txt
```

## 3. Repository structure
```bash
SOCToolbox(main)$ tree -L 2
.
├── LICENSE
├── README.md
├── reference_results
│   ├── DIS
│   └── LAVA_WAAM
├── requirements.txt
├── results
└── run
    ├── eval_DIS.py
    ├── eval_DIS_VD.py
    ├── eval_LAVA_WAAM.py
    ├── show_ref_DIS.py
    ├── show_ref_LAVA_WAAM_fine-tuned.py
    ├── show_ref_LAVA_WAAM_pretrained.py
    └── source
```

The main script for evaluating *pretrained* and *fine-tuned* models is `eval_LAVA_WAAM.py`.

Additional scripts `eval_DIS.py` and `eval_DIS_VD.py` are provided to reproduce the `ISNet.pth` results from the original [publication](https://arxiv.org/pdf/2203.03041). These scripts validate our evaluation pipeline.


## 4. Metrics calculation

0. **Generate inference results** (segmentation masks) using [DIS](https://github.com/xuebinqin/DIS?tab=readme-ov-file#ii-inference-for-dataset-withwithout-ground-truth).  
1. **Run** `eval_LAVA_WAAM.py`, specifying the correct paths:
   - `--data_dir DATA_DIR`: Path to the dataset directory.
   - `--pred_dir PRED_DIR`: directory with inference results from step 1  
2. **Compare** the results saved in `results/` against the `reference_results/`


## 5. Usage
```bash
(soc_env) SOCToolbox$ python3 run/eval_LAVA_WAAM.py --help

usage: eval_LAVA_WAAM.py [-h] [--data_dir DATA_DIR] [--pred_dir PRED_DIR]

options:
  -h, --help           show this help message and exit
  --data_dir DATA_DIR  Path to the dataset directory.
  --pred_dir PRED_DIR  Path to the predictions directory.

```

## 6. Default paths
By default, we assume that `LAVA_WAAM` and `DIS5K` datasets are stored under `/home/docker/isnet_datasets/`.
```bash
$ ls /home/docker/isnet_datasets/
DIS5K  LAVA_WAAM
```

The default location for inference results (i.e. predicted masks) used for evaluation is: `/home/docker/inference_results_isnet/`
```bash
$ ls /home/docker/inference_results_isnet/
DIS5K_isnet_pth  LAVA_WAAM_isnet_pth  LAVA_WAAM_fine-tuned_pth
```
Recommended usage of the evaluation scripts:
- Recreate the same directory structure (e.g. using symlinks), so default paths work out of the box;
or
- Explicitly pass the paths to `DATA_DIR` and `PRED_DIR` when running the evaluation scripts

## 7. Results
Evaluation results are printed to the console and saved in the `results/` directory.  
Each run generates five tables: four detailed tables and one summary table.


## 8. Reference results
Reference results are stored in the `reference_results/` directory.  
You can view them in Excel or run one of the available scripts:  
  - `show_ref_LAVA_WAAM_pretrained.py`
  - `show_ref_LAVA_WAAM_fine-tuned.py`
  - `show_ref_DIS.py`


```bash
(soc_env) SOCToolbox(main)$ python3 run/show_ref_results/show_ref_LAVA_WAAM_pretrained.py

20251008_214205_detailed_S-1.csv:
┍━━━━━┯━━━━━━━━━━━━━━━┯━━━━━━━━━┯━━━━━━━━━━━━━┯━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━┑
│ N   │ Subset        │   maxFm │   wFmeasure │   MAE │   Smeasure │   meanEm │
┝━━━━━┿━━━━━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│ 1   │ E3_S4_C1_P2_6 │   0.181 │       0.010 │ 0.145 │      0.427 │    0.252 │
│ 2   │ E5_S7_C0_P13  │   0.258 │       0.007 │ 0.212 │      0.394 │    0.251 │
│ 3   │ E5_S7_C0_P14  │   0.247 │       0.007 │ 0.202 │      0.398 │    0.251 │
│ 4   │ E5_S8_C0_P1   │   0.319 │       0.006 │ 0.265 │      0.367 │    0.251 │
│ 5   │ E5_S10_C0_P8  │   0.223 │       0.006 │ 0.181 │      0.409 │    0.251 │
┝━━━━━┿━━━━━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│     │ Average:      │   0.246 │       0.007 │ 0.201 │      0.399 │    0.251 │
┕━━━━━┷━━━━━━━━━━━━━━━┷━━━━━━━━━┷━━━━━━━━━━━━━┷━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━┙


20251008_214205_detailed_S-2.csv:
┍━━━━━┯━━━━━━━━━━━━━━━━┯━━━━━━━━━┯━━━━━━━━━━━━━┯━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━┑
│ N   │ Subset         │   maxFm │   wFmeasure │   MAE │   Smeasure │   meanEm │
┝━━━━━┿━━━━━━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│ 1   │ E3_S5_C2_P0    │   0.304 │       0.175 │ 0.065 │      0.527 │    0.400 │
│ 2   │ E3_S5_C2_P5    │   0.177 │       0.011 │ 0.142 │      0.428 │    0.252 │
│ 3   │ E4_S6_C0_P2_12 │   0.923 │       0.763 │ 0.041 │      0.810 │    0.852 │
│ 4   │ E4_S6_C0_P3    │   0.186 │       0.008 │ 0.149 │      0.425 │    0.251 │
┝━━━━━┿━━━━━━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│     │ Average:       │   0.397 │       0.239 │ 0.099 │      0.547 │    0.439 │
┕━━━━━┷━━━━━━━━━━━━━━━━┷━━━━━━━━━┷━━━━━━━━━━━━━┷━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━┙


20251008_214205_detailed_S-3.csv:
┍━━━━━┯━━━━━━━━━━━━━━━━━┯━━━━━━━━━┯━━━━━━━━━━━━━┯━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━┑
│ N   │ Subset          │   maxFm │   wFmeasure │   MAE │   Smeasure │   meanEm │
┝━━━━━┿━━━━━━━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│ 1   │ E5_S9_C1_P7     │   0.518 │       0.122 │ 0.261 │      0.408 │    0.328 │
│ 2   │ E5_S9_C1_P16    │   0.276 │       0.007 │ 0.228 │      0.385 │    0.255 │
│ 3   │ E5_S9_C1_P19    │   0.253 │       0.007 │ 0.207 │      0.396 │    0.252 │
│ 4   │ E5_S11_C2_P5    │   0.210 │       0.005 │ 0.178 │      0.406 │    0.277 │
│ 5   │ E5_S11_C2_P10_1 │   0.269 │       0.005 │ 0.222 │      0.388 │    0.251 │
│ 6   │ E5_S11_C2_P11   │   0.352 │       0.005 │ 0.295 │      0.352 │    0.251 │
┝━━━━━┿━━━━━━━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│     │ Average:        │   0.313 │       0.025 │ 0.232 │      0.389 │    0.269 │
┕━━━━━┷━━━━━━━━━━━━━━━━━┷━━━━━━━━━┷━━━━━━━━━━━━━┷━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━┙


20251008_214205_detailed_S-4.csv:
┍━━━━━┯━━━━━━━━━━━━━━━━┯━━━━━━━━━┯━━━━━━━━━━━━━┯━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━┑
│ N   │ Subset         │   maxFm │   wFmeasure │   MAE │   Smeasure │   meanEm │
┝━━━━━┿━━━━━━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│ 1   │ E6_S12_T1_A1_4 │   0.214 │       0.007 │ 0.173 │      0.413 │    0.251 │
│ 2   │ E6_S12_T1_A1_6 │   0.226 │       0.012 │ 0.184 │      0.408 │    0.254 │
│ 3   │ E6_S12_T1_B2_3 │   0.150 │       0.008 │ 0.120 │      0.439 │    0.252 │
│ 4   │ E6_S12_T1_B2_5 │   0.147 │       0.008 │ 0.117 │      0.440 │    0.252 │
┝━━━━━┿━━━━━━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│     │ Average:       │   0.184 │       0.009 │ 0.148 │      0.425 │    0.252 │
┕━━━━━┷━━━━━━━━━━━━━━━━┷━━━━━━━━━┷━━━━━━━━━━━━━┷━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━┙


20251008_214205_detailed_S-5.csv:
┍━━━━━┯━━━━━━━━━━━━━━━━┯━━━━━━━━━┯━━━━━━━━━━━━━┯━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━┑
│ N   │ Subset         │   maxFm │   wFmeasure │   MAE │   Smeasure │   meanEm │
┝━━━━━┿━━━━━━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│ 1   │ E6_S14_C2_V4   │   0.260 │       0.007 │ 0.213 │      0.393 │    0.251 │
│ 2   │ E6_S14_C2_V6_3 │   0.213 │       0.008 │ 0.173 │      0.413 │    0.251 │
│ 3   │ E6_S14_C2_V7_1 │   0.219 │       0.008 │ 0.177 │      0.411 │    0.251 │
│ 4   │ E6_S15_C3_V2_0 │   0.255 │       0.007 │ 0.209 │      0.395 │    0.251 │
│ 5   │ E6_S15_C3_V2_1 │   0.243 │       0.007 │ 0.198 │      0.400 │    0.251 │
│ 6   │ E6_S15_C3_V2_6 │   0.237 │       0.007 │ 0.193 │      0.403 │    0.251 │
┝━━━━━┿━━━━━━━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│     │ Average:       │   0.238 │       0.008 │ 0.194 │      0.402 │    0.251 │
┕━━━━━┷━━━━━━━━━━━━━━━━┷━━━━━━━━━┷━━━━━━━━━━━━━┷━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━┙


20251008_214205_summary.csv:
┍━━━━━┯━━━━━━━━━━┯━━━━━━━━━┯━━━━━━━━━━━━━┯━━━━━━━┯━━━━━━━━━━━━┯━━━━━━━━━━┑
│ N   │ Subset   │   maxFm │   wFmeasure │   MAE │   Smeasure │   meanEm │
┝━━━━━┿━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│ 1   │ S-1      │   0.246 │       0.007 │ 0.201 │      0.399 │    0.251 │
│ 2   │ S-2      │   0.397 │       0.239 │ 0.099 │      0.547 │    0.439 │
│ 3   │ S-3      │   0.313 │       0.025 │ 0.232 │      0.389 │    0.269 │
│ 4   │ S-4      │   0.184 │       0.009 │ 0.148 │      0.425 │    0.252 │
│ 5   │ S-5      │   0.238 │       0.008 │ 0.194 │      0.402 │    0.251 │
┝━━━━━┿━━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━━━━━┿━━━━━━━┿━━━━━━━━━━━━┿━━━━━━━━━━┥
│     │ Average: │   0.276 │       0.058 │ 0.175 │      0.433 │    0.292 │
┕━━━━━┷━━━━━━━━━━┷━━━━━━━━━┷━━━━━━━━━━━━━┷━━━━━━━┷━━━━━━━━━━━━┷━━━━━━━━━━┙```

```bash
(soc_env) SOCToolbox(main)$ python3 run/show_ref_LAVA_WAAM_fine-tuned.py 
# ...
```

## 9. Acknowledgements

We thank the following open-source projects for their contributions:

- [SOCToolbox](https://github.com/mczhuge/SOCToolbox)  
- [PySODMetrics](https://github.com/lartpang/PySODMetrics)  
- [SCRN](https://github.com/wuzhe71/SCRN)  

