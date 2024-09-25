def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])  # Работают, но Pycharm выдает ошибку так как функция ожидает другие значения

values_list = [66, 'шесть_шесть', True]
values_dict = {'a': 18, 'b': 'три_четыре', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'toto']
print_params(*values_list_2, 42)