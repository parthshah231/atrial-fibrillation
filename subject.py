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
        self.attr_file = Atr(atr_path)
        self.hea_file = Header(hea_path)
        self.dat_file = Dat(DATA / (self.id + ".dat"))
        self.qrs_file = Qrs(DATA / (self.id + ".qrs"))

    def func_name(self) -> Any:
        pass


# def process_subject(paths: Dict) -> Subject:
#     subject = Subject(atr_path=paths['atr_path'], hea_path=paths['hea_path'])
#     return subject


if __name__ == "__main__":
    ATR_PATHS = sorted(DATA.rglob("*.atr"))
    HEA_PATHS = sorted(DATA.rglob("*.hea"))
    subjects = [
        Subject(atr_path=atr_path, hea_path=hea_path)
        for atr_path, hea_path in tqdm(zip(ATR_PATHS, HEA_PATHS), total=len(ATR_PATHS))
    ]
    print(len(subjects))
