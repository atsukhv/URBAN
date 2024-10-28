"""
requirements.txt

requests==2.32.3
pandas==2.2.3
matplotlib==3.9.2

"""



import requests
import pandas as pd
import matplotlib.pyplot as plt

print('--')
print('REQUESTS')
print('--')
# Отправка GET-запроса
response = requests.get('https://api.github.com')

# Проверка статуса ответа
if response.status_code == 200:
    print("Данные успешно получены:")
    print(response.json())  # Выводим данные в формате JSON
else:
    print("Ошибка при получении данных:", response.status_code)


print('')
print('--')
print('PANDAS')
print('--')

# Чтение данных из CSV файла
data = pd.read_csv('urban.csv')

# Вывод первых 5 строк
print("Первые 5 строк данных:")
print(data.head())

# Простая агрегация: среднее значение по столбцу 'value'
mean_value = data['value'].mean()
print("Среднее значение по столбцу 'value':", mean_value)

# Фильтрация данных: выбор строк, где 'value' больше 10
filtered_data = data[data['value'] > 10]
print("Данные, где 'value' больше 10:")
print(filtered_data)

print('')
print('--')
print('MATPLOTLIB')
print('--')

# Пример данных
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание линейного графика
plt.plot(x, y, marker='o')
plt.title('Пример линейного графика')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

print('График успешно построен')
