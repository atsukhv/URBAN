calls = 0


def count_calls():
    global calls
    calls += 1


def string_info():
    string = input('Напишите что-то: ')
    string_length = len(string)
    string_in_upper_case = string.upper()
    string_in_lower_case = string.lower()
    list_to_search = (string_length, string_in_upper_case, string_in_lower_case)
    count_calls()
    return string, list_to_search


def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search_lower = [str(item).lower() for item in list_to_search]
    if string in list_to_search_lower:
        print(True)
    else:
        print(False)


x = 0
while x == 0:
    string, list_to_search = string_info()
    print(string, list_to_search)
    is_contains(string, list_to_search)
    print(calls)
    x = int(input('Введите "0", если хотите проверить ещё одно слово, или "1" для закрытия программы: '))
