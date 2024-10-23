from datetime import datetime
from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            i += 1
            file.write(f"Какое-то слово №{i}")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


start_funcs = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
stop_funcs = datetime.now()
funcs_res = stop_funcs - start_funcs
print(f"Время выполнения в одном потоке: {funcs_res}")

start_threads = datetime.now()

p1 = Thread(target=write_words, args=(10, 'example5.txt'))
p2 = Thread(target=write_words, args=(30, 'example6.txt'))
p3 = Thread(target=write_words, args=(200, 'example7.txt'))
p4 = Thread(target=write_words, args=(100, 'example8.txt'))

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

stop_threads = datetime.now()
print(f"Время выполнения в нескольких потоках: {stop_threads - start_threads}")