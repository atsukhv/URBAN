first = input('first: ')
second = input('second: ')
third = input('third: ')

if first == second == third:
    print("3")
elif first == second or first == third or second == third:
    print("2")
else:
    print("1")