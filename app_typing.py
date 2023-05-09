from dataclasses import dataclass
from pathlib import Path
from pandas.core.series import Series


@dataclass(slots=True, frozen=True)
class CSVFileData:
    series: Series
    title: str
    path: Path