class House:
    def __init__(self, name, number_of_floors): #Создание класса House и Вунтри класса House определяем метод __init__, в который передаем название и кол-во этажей.
        self.name = name                        # Внутри метода __init__ создаем атрибуты объекта self.name и self.number_of_floors, присваиваем им переданные значения.
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor): # Создаем метод go_to с параметром new_floor и пишем  логику внутри него на основе описания задачи.
      if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
            else:
             print("Такого этажа не существует")


# Создание объекта класса House с произвольным названием и количеством этажей.
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
