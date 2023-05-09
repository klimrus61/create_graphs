from pathlib import Path
from typing import Generator
import re


class NotValidPathError(Exception):
    '''Путь не действителен'''


class PathToFile:
    '''Работа с путями до excel и фоток'''
    def __init__(self) -> None:
        self.main_path = self.get_path()
        self.main_pic_path = self.create_main_picture_folder(self.main_path)


    def get_path(self)-> Path:
        '''Получить путь до главной папки'''
        print('Введите путь полный путь папки ТП\n'\
              'Структура папок внутри - Папка ТП\\Папки с датами\\файлы csv\n'
              'Пример: C:\\Users\\klim\\Desktop\\ТП_ГОЙТЕХ\n')
        user_input = input('Путь до папки: ')
        try:
            pathdir = Path(user_input)
            assert pathdir.is_dir()
        except Exception:
            raise NotValidPathError
        return pathdir

    def iter_date_folders(self, dirpath : Path) -> Generator[Path, None, None]:
        '''Получить список валидных папок из гланой папки'''
        for dir in dirpath.iterdir():
            if dir.is_dir():
                yield dir

    def create_main_picture_folder(self, dirpath: Path) -> Path:
        '''Создать главную папку для сриншотов графиков'''
        picture_folder = Path(dirpath.parent, 'pictures_main_folder')
        if not picture_folder.exists():
            picture_folder.mkdir()
        return picture_folder

    def create_date_pic_folder(self, sub_folder_name: str) -> Path:
        '''Создать sub folder для картинок графиков'''
        sub_folder_path = Path(self.main_pic_path, sub_folder_name)
        if not sub_folder_path.exists():
            sub_folder_path.mkdir()
        return sub_folder_path
    
    def create_parameter_folder(self, sub_folder: Path, parameter_name: str) -> Path:
        '''Создать папку для параметра'''
        parameter_name = self.sanitize_folder_name(parameter_name)
        parameter_folder = sub_folder / parameter_name
        if not parameter_folder.exists():
            parameter_folder.mkdir()
        return parameter_folder
    
    def sanitize_folder_name(self, folder_name):
        # Define the pattern to match invalid symbols
        pattern = r'[<>:"/\\|?*]'
        # Remove invalid symbols using regular expression substitution
        sanitized_name = re.sub(pattern, ' ', folder_name)
        return sanitized_name
    
    def path_to_pic(self, parameter_folder: Path, name_csv_file: str) -> Path:
        '''Получить полный путь до картинки'''
        name_pic_file = name_csv_file.replace('csv', 'png')
        path_to_pic = Path(parameter_folder, name_pic_file)
        return path_to_pic
    
    def iter_csv_files(self, date_folder: Path) -> Generator[Path, None, None]:
        '''Пройтись по файлам csv внутри папки с датами'''
        for file in date_folder.iterdir():
            if file.suffix == '.csv':
                yield file