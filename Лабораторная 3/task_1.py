class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта "Книга"

        :param name: название книги
        :param author: автор книги

        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """ Свойство getter, не позволяющее изменять атрибут"""
        return self._name

    @property
    def author(self) -> str:
        """ Свойство getter, не позволяющее изменять атрибут"""
        return self._author

    def __str__(self):
        """
        Функция, которая должна возвращать строку

        :return: строка

        """
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        """
        Функция, которая должна возвращать валидную python строку

        :return: валидная строка

        """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Бумажная книга. Дочерний класс"""
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Бумажная книга"

        :param name: название книги
        :param author: автор книги
        :param pages: количество страниц

        """
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Свойство, устанавливающее кол-во страниц с проверками при присвоении им значений"""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц это положительное значение")
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"


class AudioBook(Book):
    """ Аудиокнига. Дочерний класс """
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка к работе объекта "Аудиокнига"

        :param name: название книги
        :param author: автор книги
        :param duration: продолжительность

        """
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """Свойство, устанавливающее продолжительность с проверками при присвоении ей значения"""
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность это положительное значение")
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"


print(PaperBook("Капитанская дочка", "Пушкин", 200))
print(AudioBook("Капитанская дочка", "Пушкин", 4.2))
print(repr(PaperBook("Капитанская дочка", "Пушкин", 200)))
print(repr(AudioBook("Капитанская дочка", "Пушкин", 4.2)))
#Перенос строки