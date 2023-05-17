import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import io
from PIL import Image

from app_typing import CSVFileData


class CreatePictureError:
    '''Ошибка создания снимка графика'''


def save_graph_as_png(data_frame: CSVFileData):
    '''Сохранить график в формате png'''
    try:
        xformatter = mdates.DateFormatter('%H:%M:%S.%f')
        plt.ioff()
        plt.figure().set_figwidth(15)
        plt.plot(data_frame.series.index, data_frame.series.values)
        plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
        plt.xlabel('Время')
        # plt.ylabel(data_frame.series.name, rotation=90)
        plt.title(data_frame.series.name, loc='left')
        plt.tight_layout()
        plt.savefig(data_frame.path, format='png', dpi=300)
        plt.close()
    except Exception as e:
        print(e)
        print(data_frame.path)
        plt.close()



def save_picture(data_frame: CSVFileData) -> None:
    "Создать и сохранить картинку по данным"
    graph = _create_graph(data_frame)
    graph.savefig(data_frame.path)

def create_picture(data_frame: CSVFileData):
    '''Создать картинку png по данным для графика'''
    graph = _create_graph(data_frame)
    picture = _create_picture(graph)
    return picture

def _create_graph(data_frame: CSVFileData) -> plt:
    '''Создать график по данным'''
    fig = plt.figure(figsize=(20,4))
    plt.plot(data_frame.series)
    plt.xlabel('Время')
    plt.ylabel(data_frame.series.name)
    plt.title(data_frame.title)
    return fig
    
def _create_picture(graph: plt) -> Image:
    '''Создает фото'''
    canvas = graph.canvas
    buffer = io.BytesIO()
    canvas.print_png(buffer)
    buffer.seek(0)
    image = Image.open(buffer)
    return image


if __name__ == "__main__":
    pic = create_picture(CSVFileData([1,2,3], [10, 20, 15], 'название', 'залупы'))
    pic.show()