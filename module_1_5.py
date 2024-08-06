immutable_var = (1, 2.5, 'text', True)
print(immutable_var)

# immutable_var[0] = 10
# выдает ошибку TypeError: 'tuple' object does not support item assignment это означает что объект "кортеж" нельзя изменить

mutable_list = [10, 100.5, 'URBAN', False]
mutable_list[0] = 100
print(mutable_list)