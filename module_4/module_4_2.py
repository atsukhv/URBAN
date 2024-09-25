def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


inner_function()  # Ошибка так как эта функция не находится в области видимости глобального пространства
