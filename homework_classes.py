class Animal:
    """Модель животного"""

    def __init__(self, name, weight):
        """Инициализируется имя и вес"""
        self.name = name
        self.weight = weight

    def feed(self):
        """Кормим"""
        print(self.name.title() + " накормлен")

    def __repr__(self):
        return "Имя - " + self.name + " Вес - " + str(self.weight)


class Bird(Animal):
    """Модель птицы"""

    def pick_eggs(self):
        """Собираем яйца"""
        print("у " + self.name.title() + " собраны яйца")


class Goose(Bird):
    """Модель гуся"""

    def voice(self):
        """Гусь гогочет"""
        print(self.name.title() + " гогочет")


class Chicken(Bird):
    """Модель курицы"""

    def voice(self):
        """Курица кудахчет"""
        print(self.name.title() + " кудахчет")


class Duck(Bird):
    """Модель утки"""

    def voice(self):
        """Утка крякает"""
        print(self.name.title() + " крякает")


class Cow(Animal):
    """Модель коровы"""

    def milk(self):
        """Доим"""
        print(self.name.title() + " подоена")

    def voice(self):
        """Корова мычит"""
        print(self.name.title() + " мычит")


class Goat(Animal):
    """Модель козы"""

    def milk(self):
        """Доим"""
        print(self.name.title() + " подоена")

    def voice(self):
        """Коза мекает"""
        print(self.name.title() + " мекает")


class Sheep(Animal):
    """Модель овцы"""

    def cut(self):
        """Стрижем"""
        print(self.name.title() + " подстрижена")

    def voice(self):
        """Овца блеет"""
        print(self.name.title() + " блеет")


all_animals = {"Серый": Goose("Серый", 10)}
all_animals.get("Серый").voice()
all_animals.get("Серый").feed()
all_animals.get("Серый").pick_eggs()

all_animals["Белый"] = Goose("Белый", 9)
all_animals.get("Белый").voice()
all_animals.get("Белый").feed()
all_animals.get("Белый").pick_eggs()

all_animals["Ко-ко"] = Chicken("Ко-ко", 1)
all_animals.get("Ко-ко").voice()
all_animals.get("Ко-ко").feed()
all_animals.get("Ко-ко").pick_eggs()

all_animals["Кукареку"] = Chicken("Кукареку", 2)
all_animals.get("Кукареку").voice()
all_animals.get("Кукареку").feed()
all_animals.get("Кукареку").pick_eggs()

all_animals["Кряква"] = Duck("Кряква", 1.5)
all_animals.get("Кряква").voice()
all_animals.get("Кряква").feed()
all_animals.get("Кряква").pick_eggs()

all_animals["Манька"] = Cow("Манька", 500)
all_animals.get("Манька").voice()
all_animals.get("Манька").feed()
all_animals.get("Манька").milk()

all_animals["Рога"] = Goat("Рога", 140)
all_animals.get("Рога").voice()
all_animals.get("Рога").feed()
all_animals.get("Рога").milk()

all_animals["Копыта"] = Goat("Копыта", 130)
all_animals.get("Копыта").voice()
all_animals.get("Копыта").feed()
all_animals.get("Копыта").milk()

all_animals["Барашек"] = Sheep("Барашек", 160)
all_animals.get("Барашек").voice()
all_animals.get("Барашек").feed()
all_animals.get("Барашек").cut()

all_animals["Кудрявый"] = Sheep("Кудрявый", 185)
all_animals.get("Кудрявый").voice()
all_animals.get("Кудрявый").feed()
all_animals.get("Кудрявый").cut()

overall_weight = 0
for beast in all_animals.values():
    overall_weight += beast.weight
print(overall_weight)

fattest_animal = ""
fattest_animal_weight = 0
for beast in all_animals.values():
    if fattest_animal_weight < beast.weight:
        fattest_animal = beast.name
        fattest_animal_weight = beast.weight
print(fattest_animal)

print(all_animals)