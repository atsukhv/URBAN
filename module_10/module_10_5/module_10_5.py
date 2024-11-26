import multiprocessing
from datetime import datetime

# Список файлов для чтения
files = ['./file1.txt',
         './file2.txt',
         './file3.txt',
         './file4.txt']


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return

if __name__ == '__main__':
    # Линейный вызов
    time_start = datetime.now()
    for file in files:
        read_info(file)
    time_end = datetime.now()
    print(f"Время выполнения в одном потоке: {time_end - time_start}")

    # Многопроцессный вызов
    time_start = datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, files)
    time_end = datetime.now()
    print(f"Время выполнения в мультипотоке: {time_end - time_start}")
