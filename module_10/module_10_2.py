import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        soldiers = 100
        days = 0
        print(f'{self.name} на нас напали')
        while soldiers > 0:
            soldiers -= self.power
            time.sleep(1)
            days += 1
            if soldiers <= 0:
                print(f'{self.name} одержал победу спустя {days} дней(дня)!')
            else:
                print(f'{self.name} сражался {days}..., осталось {soldiers} войнов\n')


threads = []

thred_1 = Knight('papania', 25)
thred_2 = Knight('Artur', 5)
thred_3 = Knight('SiDzinPin', 15)

threads.append(thred_1)
threads.append(thred_2)
threads.append(thred_3)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
