from pathlib import Path
import pandas as pd

from app_typing import CSVFileData


class ParseDataError(Exception):
    '''Ошибка получения данных'''


def parse_data_from_csv(csv_path: Path) -> pd.DataFrame:
    '''Получить все данные из csv файла'''
    try:
        df = pd.read_csv(csv_path, delimiter=';', header=1, decimal=',', index_col=0, encoding='utf-8')
        df.index = pd.to_datetime(df.index, format='%H:%M:%S.%f')
        return df
    except Exception:
        raise ParseDataError

def get_all_parameters(csv_path: Path) -> list[str]:
    '''Получить параметры csv'''
    df = pd.read_csv(csv_path, delimiter=';', header=1, nrows=0)
    return df.columns.to_list()


if __name__ == "__main__":
    parse_data_from_csv(r'C:\Users\klim\Desktop\готех\01.2023\Гойтх_01_01_2023.csv')