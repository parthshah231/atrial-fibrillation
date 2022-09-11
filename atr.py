from pathlib import Path
from typing import Any

import numpy as np
from tqdm import tqdm
from wfdb.io import ann2rr

from constants import DATA

ATR_PATHS = sorted(DATA.rglob("*.atr"))


class Atr:
    """I have no idea what the array here is giving me.
    Look more into it."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.file_name = str(self.path).split(".")[0]
        # self.atr_locations = self.parse()

    def read(self) -> np.ndarray:
        atr = ann2rr(self.file_name, "atr")
        return atr


if __name__ == "__main__":
    atrs = [Atr(atr_path) for atr_path in tqdm(ATR_PATHS)]
    print("Debug")
