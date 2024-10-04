import math

class Figure:
    def __init__(self, color: list, *sides):
        self.sides_count = 0
        self.__sides = list(sides)
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print('Цвет не существует в палитре RGB')

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides * self.sides_count

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print('Количество сторон не может быть равно количеству сторон фигуры')


class Circle(Figure):
    def __init__(self, color: list, *sides):
        super().__init__(color, *sides)
        self.sides_count = 1
        if len(sides) == 0:
            self.__sides = [1]  # Устанавливаем радиус по умолчанию

    def get_radius(self):
        return self.__sides[0]

    def get_square(self):
        radius = self.get_radius()
        return math.pi * radius ** 2


class Triangle(Figure):
    def __init__(self, color: list, *sides):
        super().__init__(color, *sides)
        self.sides_count = 3
        if len(sides) == 0:
            self.__sides = [1, 1, 1]  # Устанавливаем стороны по умолчанию

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    def __init__(self, color: list, *sides):
        super().__init__(color, *sides)
        self.sides_count = 12
        if len(sides) == 0:
            self.__sides = [1] * 12  # Устанавливаем стороны по умолчанию
        else:
            side = sides[0]
            self.__sides = [side] * 12

    def get_volume(self):
        side = self.__sides[0]
        return side ** 3




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())