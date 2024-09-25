my_dict = {'name': 'Albert', 'age': 20, 'is_student': True}
print(my_dict)

print(my_dict.get('name'), my_dict.get('lesson'))

my_dict['lesson'] = 'Python'
my_dict['date'] = '10.10.2022'
print(my_dict)

a = my_dict.pop('date')
print(a)
print(my_dict)

my_set = {1, 2.5, 'text', 1, 2.5, 7, 14.7, 1, 1, 1, 'text'}
print(my_set)

my_set.add(14)
my_set.add(3)
my_set.remove(1)
print(my_set)
