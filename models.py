class Animal(object):
    def __init__(self, name: str, age: int, typ: str):
        self._name = name
        self._age = age
        self._typ = typ  # Тип животного

    def __str__(self):
        return f"{self._name} -> {self._age} лет"

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_typ(self):
        return self._typ


class Giraffe(Animal):
    def __init__(self, name: str, age: int, color: str, aviary: int):
        super().__init__(name, age, 'жираф')
        self._color = color
        self._aviary = aviary  # Номер вольера

    def __str__(self):
        return f"Жираф {super().__str__()} он {self._color} и живет в {self._aviary} вольере"

    def get_color(self):
        return self._color

    def get_aviary(self):
        return self._aviary

    def set_aviary(self, new_aviary):
        self._aviary = new_aviary  # Поменять номер вольера
        print(f"{self.get_name()} был переселен в -> {self._aviary} вольер")


class Zebra(Animal):
    def __init__(self, name: str, age: int, color: str, aviary: int):
        super().__init__(name, age, 'зебра')
        self._color = color
        self._aviary = aviary

    def __str__(self):
        return f"Зебра {super().__str__()} он {self._color} и живет в {self._aviary} вольере"

    def get_color(self):
        return self._color

    def get_aviary(self):
        return self._aviary

    def set_aviary(self, new_aviary):
        self._aviary = new_aviary
        print(f"{self.get_name()} был переселен в -> {self._aviary} вольер")


class Lion(Animal):
    def __init__(self, name: str, age: int, color: str, aviary: int):
        super().__init__(name, age, 'лев')
        self._color = color
        self._aviary = aviary  # Номер вольера

    def __str__(self):
        return f"Лев {super().__str__()} он {self._color} и живет в {self._aviary} вольере"

    def get_color(self):
        return self._color

    def get_aviary(self):
        return self._aviary

    def set_aviary(self, new_aviary):
        self._aviary = new_aviary  # Поменять номер вольера
        print(f"{self.get_name()} был переселен в -> {self._aviary} вольер")


class SmallLion(Lion):
    def __init__(self, name: str, age: int, aviary: int, voice: str, diet: str):
        super().__init__(name, age, 'бордовый', aviary)
        self._voice = voice
        self._diet = diet

    def __str__(self):
        return f"Маленький {super().__str__()}. Он рычит-> {self._voice}. {self.get_name()} ест {self._diet}"

    def get_voice(self):
        return self._voice

    def get_diet(self):
        return self._diet

    def set_diet(self, new_diet):
        self._diet = new_diet
        print(f"Диета изменена, теперь {self.get_name()} ест {self._diet}")


class WildLion(Lion):
    def __init__(self, name: str, age: int, aviary: int, voice: str, diet: str):
        super().__init__(name, age, 'темно коричневый', aviary)
        self._voice = voice
        self._diet = diet

    def __str__(self):
        return f"Дикий  {super().__str__()}. Ричит-> {self._voice}. {self.get_name()} ест {self._diet}"

    def get_voice(self):
        return self._voice

    def get_diet(self):
        return self._diet

    def set_diet(self, new_diet):
        self._diet = new_diet
        print(f"Диета изменена, теперь {self.get_name()} ест {self._diet}")
