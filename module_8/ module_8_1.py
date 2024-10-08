def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        try:
            result_ = float(a) + float(b)
            if result_ % 1 == 0:
                return int(result_)
            return result_
        except ValueError:
            return str(a) + str(b)


print(add_everything_up('3', 8.7))
print(add_everything_up(3, '3.6'))
print(add_everything_up('URBAN', 8.1))
