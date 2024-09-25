def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(3, 7, 5)
result2 = get_matrix(2, 4, 42)
result3 = get_matrix(9, 1, 13)
print(result1)
print(result2)
print(result3)