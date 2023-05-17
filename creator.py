from files_worker import PathToFile
from parse import parse_data_from_csv, get_all_parameters
from visualization import save_graph_as_png
from app_typing import CSVFileData


def main():
    print('Начало работы\n'\
          'Консольная программа для построения графиков\n')
    path_worker = PathToFile()
    parameters = None
    if path_worker.check_config_exist():
        parameters = get_all_parameters(path_worker.main_path / 'config.csv')
    for subdir in path_worker.iter_date_folders(path_worker.main_path):
        print(f'Начало обработка даты {subdir.name}')
        pic_date_dir = path_worker.create_date_pic_folder(subdir.name)
        for csv_file in path_worker.iter_csv_files(subdir):
            print(f'Парсинг файла {csv_file.name}')
            df = parse_data_from_csv(csv_file)
            if parameters is not None:
                df.columns = parameters
            for column in df.columns:
                parameter_folder = path_worker.create_parameter_folder(pic_date_dir, parameter_name=column)
                path_to_pic = path_worker.path_to_pic(parameter_folder, csv_file.name)
                data_to_visual = CSVFileData(series=df[column], title=csv_file.name, path=path_to_pic)
                save_graph_as_png(data_to_visual)
    print('Конец работы')

if __name__ == "__main__":
    main()