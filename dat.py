from pathlib import Path
from tracemalloc import start
from typing import Any, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import wfdb
from tqdm import tqdm

from constants import DATA

DAT_PATHS = sorted(DATA.rglob("*.dat"))


class Dat:
    def __init__(self, path: Path) -> None:
        """Contains information/waveforms of a subject associated to the
        corresponding header_file (ex: 00.hea)"""
        self.path = path
        self.file_name = str(self.path).split(".")[0]
        self.start_time, self.end_time, self.hrs, self.sig_len, self.frequency = self.parse()

    def parse(self) -> Tuple[pd.Timestamp, pd.Timestamp, float, int, int]:
        _, info_dict = wfdb.rdsamp(self.file_name)
        frequency = info_dict["fs"]
        sig_len = info_dict["sig_len"]
        start_date = info_dict["base_date"]
        year, month, day = start_date.year, start_date.month, start_date.day
        start_t = info_dict["base_time"]
        hr, min, sec = start_t.hour, start_t.minute, start_t.second
        start_time = pd.to_datetime(f"{year}-{month}-{day} {hr}:{min}:{sec}")
        hrs = sig_len / (frequency * 60 * 60)
        end_time = start_time + pd.Timedelta(hours=hrs)
        return start_time, end_time, hrs, sig_len, frequency

    def read(self) -> np.ndarray:
        """Return wave data"""
        waves, _ = wfdb.rdsamp(self.file_name)
        return waves

    def show_wave(self) -> None:
        # fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True)
        # ax[0].plot(self.waves[:, 0])
        # ax[1].plot(self.waves[:, 1])
        # ax[0].hist(self.waves.flatten())
        # plt.show()
        pass


if __name__ == "__main__":
    dats = [Dat(dat_path) for dat_path in tqdm(DAT_PATHS[:2])]
    # dats[0].show_wave()
    print("Debug")
