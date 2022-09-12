from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sbn
from numpy import ndarray
from pandas import DataFrame, Series
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map

from atr import Atr
from constants import DATA, ROOT
from dat import Dat
from header import Header
from qrs import Qrs


class Subject:
    def __init__(self, atr_path: Path, hea_path: Path) -> None:
        self.id = atr_path.stem
        self.atr_file = Atr(atr_path)
        self.hea_file = Header(hea_path)
        self.dat_file = Dat(DATA / (self.id + ".dat"))
        self.qrs_file = Qrs(DATA / (self.id + ".qrs"))

    def func_name(self) -> Any:
        pass

    # def process_subject(paths: Dict) -> Subject:
    #     subject = Subject(atr_path=paths["atr_path"], hea_path=paths["hea_path"])
    #     return subject

    def plot_waves(self) -> None:
        waves = self.dat_file.read()
        hrs = self.dat_file.hrs
        sig_len = self.dat_file.sig_len
        x_hrs = np.linspace(0, hrs, sig_len)
        n_sig = self.hea_file.n_sig
        ax: plt.Axes
        fig, ax = plt.subplots(nrows=n_sig, ncols=1, sharex=True, figsize=(13, 7))
        fig.suptitle(f"Subject: {self.id} (ECG recordings)")
        for i in range(n_sig):
            ax[i].plot(x_hrs, waves[:, i])
            ax[i].plot(x_hrs, waves[:, i])
            ax[i].set_xlabel("Time (in hrs)")
        plt.show()


if __name__ == "__main__":
    ATR_PATHS = sorted(DATA.rglob("*.atr"))[:2]
    HEA_PATHS = sorted(DATA.rglob("*.hea"))[:2]
    subjects: List[Subject] = [
        Subject(atr_path=atr_path, hea_path=hea_path)
        for (atr_path, hea_path) in tqdm(zip(ATR_PATHS, HEA_PATHS), total=len(ATR_PATHS))
    ]
    subjects[0].plot_waves()
    # Might be helpful on a different machine
    # paths_ = []
    # for atr_path, hea_path in tqdm(zip(ATR_PATHS, HEA_PATHS), total=len(ATR_PATHS)):
    #     paths = {"atr_path": atr_path, "hea_path": hea_path}
    #     paths_.append(paths)

    # subjects = process_map(process_subject, paths_, desc="Loading subjects")
    # print("Done.")
