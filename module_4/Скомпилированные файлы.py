from dis import dis


def func():
    a = 'я функция'
    print('я функция')
    return a

dis(func)