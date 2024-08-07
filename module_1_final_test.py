grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
results = []  # список с средними баллами

students = list(students)  # преобразование множества в список
students.sort()  # сортировка по алфавиту

for sublist in grades:
    quantity = len(sublist)  # вычисляем количество оценок в подсписке
    summ = sum(sublist)  # вычисляем сумму оценок
    result = summ / quantity  # вычисляем средний балл
    results.append(result)  # добавляем средний балл в список

print(dict(zip(students, results)))  # объединяем списки в словарь и выводим значение в консоль
