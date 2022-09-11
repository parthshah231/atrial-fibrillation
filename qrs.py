from pathlib import Path
from typing import Any

import wfdb
from tqdm import tqdm

from constants import DATA

QRS_PATHS = sorted(DATA.rglob("*.qrs"))


class Qrs:
    def __init__(self, path: Path) -> None:
        """Annotations file corresponding to a subject
        waveform. Contains information about annotations
        and annotations locations relative to the beginning
        of the record."""

        self.path = path
        self.file_name = str(self.path).split(".")[0]

    def parse(self) -> Any:
        record = wfdb.rdann(self.file_name, "qrs")
        # annotations len
        ann_len = record.ann_len
        # annotation locations in samples relative
        # to the beginning of the record.
        sample = record.sample
        # annotations
        symbol = record.symbol
        frequency = record.fs
        return ann_len, sample, symbol, frequency


if __name__ == "__main__":
    qrs = [Qrs(qrs_path) for qrs_path in tqdm(QRS_PATHS)]
    # x = qrs[0].parse()
    print("Debug")
