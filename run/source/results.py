import csv
from pathlib import Path

import numpy as np
import source.metrics as M
from show_ref_results.utils import print_table


class Results:
    def __init__(self, subset: str):
        self.subset = subset

        self.FM = M.Fmeasure()
        self.WFM = M.WeightedFmeasure()
        self.MAE = M.MAE()
        self.SM = M.Smeasure()
        self.EM = M.Emeasure()

    def step(self, pred: np.ndarray, gt: np.ndarray):
        self.FM.step(pred=pred, gt=gt)
        self.WFM.step(pred=pred, gt=gt)
        self.SM.step(pred=pred, gt=gt)
        self.EM.step(pred=pred, gt=gt)
        self.MAE.step(pred=pred, gt=gt)

    def print(self):
        fm = self.FM.get_results()["fm"]
        wfm = self.WFM.get_results()["wfm"]
        sm = self.SM.get_results()["sm"]
        em = self.EM.get_results()["em"]
        mae = self.MAE.get_results()["mae"]

        self._simple_print(fm=fm, wfm=wfm, sm=sm, em=em, mae=mae)

    def _simple_print(
        self, fm: float, wfm: float, sm: float, em: float, mae: float
    ):
        print(
            (
                f"Subset: {self.subset} || maxFm: {fm['curve'].max():.3f}; wFmeasure: {wfm:.3f}; MAE: {mae:.3f}; Smeasure: {sm:.3f}; meanEm: {'-' if em['curve'] is None else em['curve'].mean():.3f};"
            )
        )


class Average:
    def __init__(self, file_name: str):
        self._subset = ""
        self._max_fm = []
        self._wfm = []
        self._mae = []
        self._sm = []
        self._mean_em = []
        # results:
        self.results_max_fm = 0
        self.results_wfm = 0
        self.results_mae = 0
        self.results_sm = 0
        self.results_mean_em = 0

        # csv:
        self.csv_path = Path(f"./results/{file_name}.csv")
        self._write_csv_header()

    def _write_csv_header(self):
        with open(self.csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "N",
                    "Subset",
                    "maxFm",
                    "wFmeasure",
                    "MAE",
                    "Smeasure",
                    "meanEm",
                ]
            )
        self._count = 0

    def _write_cvs_row(
        self,
        subset_name,
        maxFm,
        wFmeasure,
        MAE,
        Smeasure,
        meanEm,
        is_last_row=False,
    ):
        if is_last_row is False:
            self._count += 1
            count_value = self._count
        else:
            count_value = ""

        with open(self.csv_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    count_value,
                    subset_name,
                    np.round(maxFm, 3),
                    np.round(wFmeasure, 3),
                    np.round(MAE, 3),
                    np.round(Smeasure, 3),
                    np.round(meanEm, 3),
                ]
            )

    def add(
        self,
        subset: str,
        maxFm: np.float64,
        wfm: np.float64,
        mae: np.float64,
        sm: np.float64,
        meanEm: np.float64,
    ):
        self._max_fm.append(maxFm)
        self._wfm.append(wfm)
        self._mae.append(mae)
        self._sm.append(sm)
        self._mean_em.append(meanEm)

        self._write_cvs_row(
            subset_name=subset,
            maxFm=maxFm,
            wFmeasure=wfm,
            MAE=mae,
            Smeasure=sm,
            meanEm=meanEm,
        )

    def calc(self):
        self.results_max_fm = np.mean(self._max_fm)
        self.results_wfm = np.mean(self._wfm)
        self.results_mae = np.mean(self._mae)
        self.results_sm = np.mean(self._sm)
        self.results_mean_em = np.mean(self._mean_em)

        # add summary as last row
        self._write_cvs_row(
            subset_name="Average:",
            maxFm=self.results_max_fm,
            wFmeasure=self.results_wfm,
            MAE=self.results_mae,
            Smeasure=self.results_sm,
            meanEm=self.results_mean_em,
            is_last_row=True,
        )

    def print_summary(self):
        print(
            (
                f"average -> maxFm: {self.results_max_fm:.3f}; wFmeasure: {self.results_wfm:.3f}; MAE: {self.results_mae:.3f}; Smeasure: {self.results_sm:.3f}; meanEm: {self.results_mean_em:.3f};"
            )
        )


class MultiAverage(Average):
    def __init__(self, multi_average: dict[str, Average], file_name: str):
        Average.__init__(self, file_name)

        for subset_name, average in multi_average.items():
            self.add(
                subset=subset_name,
                maxFm=np.float64(average.results_max_fm),
                wfm=np.float64(average.results_wfm),
                mae=np.float64(average.results_mae),
                sm=np.float64(average.results_sm),
                meanEm=np.float64(average.results_mean_em),
            )

        self.calc()
        print_table(csv_path=self.csv_path)
