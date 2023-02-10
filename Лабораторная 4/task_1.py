class Stove:
    """Базовый класс (кухонной) плиты"""
    def __init__(self, price: float, colour: str, max_temp: int):
        """
        Создание и подготовка к работе объекта "Плита"

        :param price: цена в тыс.руб.
        :param colour: цвет
        :param max_temp: максимальная температура

        """
        self._price = price
        self.colour = colour
        self._max_temp = max_temp

    # Для атрибутов цены и температуры пропишем свойства, так как на них накладываются ограничения
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        """Свойство, устанавливающее цену с проверками при присвоении значения"""
        if not isinstance(price, float):
            raise TypeError("Цена должна быть типа float")
        if price <= 0:
            raise ValueError("Цена исключительно положительное значение")
        self._price = price

    @property
    def max_temp(self) -> int:
        return self._max_temp

    @max_temp.setter
    def max_temp(self, max_temp: int) -> None:
        """Свойство, устанавливающее макимальную температуру с проверками при присвоении значения"""
        if not isinstance(max_temp, int):
            raise TypeError("Температура должна быть типа int")
        if max_temp <= 0:
            raise ValueError("Температура исключительно положительное значение")
        self._max_temp = max_temp

    def __str__(self) -> str:
        """
        Функция, которая должна возвращать строку

        :return: строка

        """
        return f"Плита стоимостью {self._price} тыс.руб., цвет: {self.colour}," \
               f" максимальная температура: {self._max_temp} градусов"

    def __repr__(self) -> str:
        """
        Функция, которая должна возвращать валидную python строку

        :return: валидная строка

        """
        return f"{self.__class__.__name__}(price={self._price}, colour={self.colour!r}," \
               f" max_temp={self._max_temp})"

    def __eq__(self, other) -> bool:
        """Функция сверяет цвета разных плит"""
        return self.colour == other.colour

    def best_option(self, new_price: float) -> None:
        """Функция, определяющая лучший вариант при сравнении"""
        if self._price > new_price:
            print("Новый вариант плиты дешевле и рекомендован к покупке")
        if self._price <= new_price:
            print("Новый вариант плиты по цене уступает старому, не рекомендован к покупке")


class GasStove(Stove):
    """Газовая плита. Дочерний класс"""
    def __init__(self, price: float, colour: str, max_temp: int, lattice_material: str):
        """
        Создание и подготовка к работе объекта "Газовая плита"

        :param price: цена в тыс.руб.
        :param colour: цвет
        :param max_temp: максимальная температура
        :param lattice_material: материал решетки

        """
        super().__init__(price, colour, max_temp)
        self.lattice_material = lattice_material

    def __repr__(self) -> str:
        """
        Перегружаем метод __repr__, так как появился новый атрибут

        :return: валидная строка

        """
        return f"{self.__class__.__name__}(price={self._price}, colour={self.colour!r}," \
               f" max_temp={self._max_temp}, lattice_material={self.lattice_material!r})"


class ElectricStove(Stove):
    """Электрическая плита. Дочерний класс"""
    def __init__(self, price: float, colour: str, max_temp: int, power_consumption: int):
        """
        Создание и подготовка к работе объекта "Электрическая плита"

        :param price: цена в тыс.руб.
        :param colour: цвет
        :param max_temp: максимальная температура
        :param power_consumption: потребляемая мощность в Вт

        """
        super().__init__(price, colour, max_temp)
        self._power_consumption = power_consumption

    # Для атрибута потребляемой мощности пропишем свойства, так как на нее накладываются ограничения
    @property
    def power_consumption(self) -> int:
        return self._power_consumption

    @power_consumption.setter
    def power_consumption(self, power_consumption: int) -> None:
        """Свойство, устанавливающее потребляемую мощность с проверками при присвоении значения"""
        if not isinstance(power_consumption, int):
            raise TypeError("Мощность должна быть типа int")
        if power_consumption <= 0:
            raise ValueError("Мощность исключительно положительное значение")
        self._power_consumption = power_consumption

    def __repr__(self) -> str:
        """
        Перегружаем метод __repr__, так как появился новый атрибут

        :return: валидная строка

        """
        return f"{self.__class__.__name__}(price={self._price}, colour={self.colour!r}," \
               f" max_temp={self._max_temp}, power_consumption={self._power_consumption})"

    def best_option(self, new_price: float) -> None:
        """Функция, определяющая лучший вариант при сравнении.
        Перегружаем метод, так как при сравнении хотим предупредить,
        что стоит обратить внимание и на потребляемую мощность"""
        if self._price > new_price:
            print("Новый вариант плиты дешевле. Однако, стоит обратить внимание на потребляемую мощность.")
        if self._price <= new_price:
            print("Новый вариант плиты по цене уступает старому. Однако,"
                  " стоит обратить внимание на потребляемую мощность.")


if __name__ == "__main__":
    stove_1 = Stove(15.2, "белый", 275)
    print(stove_1)
    print(repr(stove_1))
    e_stove_1 = ElectricStove(20.3, "черный", 275, 8000)
    e_stove_2 = ElectricStove(20.5, "черный", 270, 8600)
    print(e_stove_1 == e_stove_2)
    e_stove_1.best_option(20.1)
    stove_1.best_option(15.3)
#Перенос строки