class Vehicle:
    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color
        self._COLOR_VARIANTS = ["blue", "red", "green"]

    def get_model(self):
        return f'Модель: {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        new_color = new_color.lower()
        if new_color in self._COLOR_VARIANTS:
            self._color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)
        __PASSENGERS_LIMIT = 5


my_car = Sedan('Альберт', 'KIA Ceed', 134, 'Silver')
my_car.print_info()

my_car.set_color('YElloW')
my_car.set_color('blUe')

my_car.owner = 'Серёга'
my_car.print_info()