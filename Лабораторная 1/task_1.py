import doctest

class Auditorium:
    def __init__(self, seating: int, spectators: int):
        """
        Создание и подготовка к работе объекта "Зрительный зал"

        :param seating: сидячие места
        :param spectators: зрители

        Примеры:
        >>> auditorium = Auditorium(300, 150)
        """
        if not isinstance(seating, int):
            raise TypeError('Сидячие места должны быть типа int')
        if seating < 0:
            raise ValueError('Количество сидячих мест является положительным числом')
        self.seating = seating

        if not isinstance(spectators, int):
            raise TypeError('Количество зрителей должно быть типа int')
        if spectators < 0:
            raise ValueError('Количество зрителей является положительным числом')
        self.spectators = spectators

    def capacity_auditorium(self) -> bool:
        """
        Функция, которая проверяет, вместится ли заданное количество людей в зале

        :return: Вместится ли заданное количество людей в зале

        Примеры:
        >>> auditorium = Auditorium(300, 150)
        >>> auditorium.capacity_auditorium()
        """
        ...
    def ticket_return(self, ticket: int) -> None:
        """
        Функция, которая уменьшает количество людей в соотвествии со сданными билетами

        :param ticket: количество сданных билетов

        :raise ValueError: Если количество сданных билетов превышает изначальное количество людей, то вызываем ошибку

        Примеры:
        >>> auditorium = Auditorium(300, 150)
        >>> auditorium.ticket_return(5)
        """
        if not isinstance(ticket, int):
            raise TypeError('Количество сданных билетов должно быть типа int')
        if ticket < 0:
            raise ValueError('Количество сданных билетов должно быть положительным числом')
        ...

class Changes:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Имя"

        :param name: имя
        :param age: возраст

        Примеры:
        >>> changes = Changes("Егор", 25)
        """
        if not isinstance(name, str):
            raise TypeError('Имя должно быть типа str')
        self.name = name

        if not isinstance(age, int):
            raise TypeError('Возраст должен быть типа int')
        self.age = age

    def possibility_changing(self) -> bool:
        """
        Функция, которая по возрасту будет проверять возможность поменять имя

        :return: Возможность смены имени

        Примеры:
        >>> changes = Changes("Егор", 25)
        >>> changes.possibility_changing()
        """
        ...

    def name_change(self, new_name: str) -> None:
        """
        Функция, которая меняет имя

        :param new_name: новое имя

        Примеры:
        >>> changes = Changes("Егор", 25)
        >>> changes.name_change("Кирилл")
        """
        if not isinstance(new_name, str):
            raise TypeError('Новое имя должно быть типа str')
        ...

class Fridge:
    def __init__(self, capacity: int, temperature: int, filling: list):
        """
        Создание и подготовка к работе объекта "Холодильник"
        
        :param capacity: вместимость
        :param temperature: температура
        :param filling: наполнение

        Примеры:
        >>> fridge = Fridge(250, 4, ['яблоко', 'малина'])
        """
        if not isinstance(capacity, int):
            raise TypeError('Вместимость должна быть типа int')
        if capacity < 0:
            raise ValueError('Вместимость это положительная величина')
        self.capacity = capacity

        if not isinstance(temperature, int):
            raise TypeError('Темпаратура должна быть типа int')
        self.temperature = temperature

        if not isinstance(filling, list):
            raise TypeError('Наполнение должно быть типа list')
        self.filling = filling

    def is_available(self, product: str) -> bool:
        """
        Функция, которая проверяет, есть ли заданный продукт в холодильнике

        :param product: продукт

        Примеры:
        >>> fridge = Fridge(250, 4, ['яблоко', 'малина'])
        >>> fridge.is_available('колбаса')
        """
        if not isinstance(product, str):
            raise TypeError('Искомый продукт должен быть типа str')
        ...

    def set_temperature(self, new_temperature: int) -> None:
        """
        Функция устанавливает температуру для холодильника

        :param new_temperature: задаваемая температура (новая)

        Примеры:
        >>> fridge = Fridge(250, 4, ['яблоко', 'малина'])
        >>> fridge.set_temperature(3)
        """
        if not isinstance(new_temperature, int):
            raise TypeError('Задаваемая температура должна быть типа int')
        ...

if __name__ == "__main__":
    doctest.testmod()
#Перенос строки 