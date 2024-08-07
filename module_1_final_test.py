grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
results = []  # список со средними баллами

students = list(students)  # преобразование множества в список
students.sort()  # сортировка по алфавиту

# линейный способ ----------------------------
# results = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
#            sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
# ---------------------------------------------

for sublist in grades:
    quantity = len(sublist)  # вычисляем количество оценок в подсписке
    summ = sum(sublist)  # вычисляем сумму оценок
    result = summ / quantity  # вычисляем средний балл
    results.append(result)  # добавляем средний балл в список

print(dict(zip(students, results)))  # объединяем списки в словарь и выводим значение в консоль
