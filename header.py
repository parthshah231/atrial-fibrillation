from pathlib import Path
from typing import Any

from tqdm import tqdm
from wfdb.io import rdheader

from constants import DATA

HEA_PATHS = sorted(DATA.rglob("*.hea"))


class Header:
    """Stores information of a header file (ex: 00.hea)
    and the dat file that it links to.

    Sample header file:
    ------------------

    00 2 128 9661440  9:30:00 31/01/2003
    00.dat 16 166.945/mV 0 0 -1 -8202 0 ECG
    00.dat 16 173.01/mV 0 0 3 6311 0 ECG

    00 - subject
    2  - n_signal
    128 - frequency
    9661440 - sig_len
    9:30:00 - start_time
    31/01/2003 - start_date

    The following two lines are segments:
    Each segment contains some info associated to
    the corresponding header file.

    """

    def __init__(self, path: Path) -> None:
        self.path = path
        self.file_name = str(self.path).split(".")[0]
        self.freq, self.start_date, self.start_time, self.sig_len = self.parse()

    def parse(self) -> Any:
        header = rdheader(self.file_name)
        frequency = header.fs
        start_date = header.base_date
        start_time = header.base_time
        sig_len = header.sig_len
        return frequency, start_date, start_time, sig_len


if __name__ == "__main__":
    headers = [Header(hea_path) for hea_path in tqdm(HEA_PATHS)]
    print("Debug")
