class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не ест {food.name}")


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


class Mammal(Animal):
    pass
    # def eat(self, food):
    #     if isinstance(food, Plant):
    #         if food.edible:
    #             print(f"{self.name} съел {food.name}")
    #             self.fed = True
    #         else:
    #             print(f"{self.name} не стал есть {food.name}")
    #             self.fed = False
    #     else:
    #         print(f"{self.name} не ест {food.name}")


class Predator(Animal):
    pass
    # def eat(self, food):
    #     if isinstance(food, Plant):
    #         if food.edible:
    #             print(f"{self.name} съел {food.name}")
    #             self.fed = True
    #         else:
    #             print(f"{self.name} не стал есть {food.name}")
    #             self.fed = False
    #     else:
    #         print(f"{self.name} не ест {food.name}")


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


bear = Predator("Медведь")
fox = Mammal("Лиса")

rabbit = Mammal('Кролик')
capibara = Mammal('Капибара')

rose = Flower('Роза')
lily = Flower('Лилия')

banana = Fruit('Банан')
mango = Fruit('Манго')

print(bear.name)
print(fox.name)
print(rabbit.name)
print(capibara.name)
print(' ')
print(rose.name)
print(lily.name)
print(banana.name)
print(mango.name)
print(' ')
print(bear.alive)
print(fox.alive)
print(' ')
print(capibara.fed)
print(rabbit.fed)
print(' ')
bear.eat(rose)
fox.eat(mango)
capibara.eat(lily)
rabbit.eat(banana)

print(' ')
print(bear.alive)
print(fox.alive)
print(rabbit.alive)
print(capibara.alive)
