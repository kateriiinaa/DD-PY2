BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id_: идентификатор книги
        :param name: название книги
        :param pages: количество страниц в книге

        """
        if not isinstance(id_, int):
            raise TypeError('Идентификатор книги должен быть типа int')
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError('Количество страниц в книге должно быть типа int')
        self.pages = pages

    def __str__(self) -> str:
        """
        Функция, которая должна возвращать строку  формата,
        где "название_книги" берется с помощью атрибута name

        :return: строка

        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Функция, которая должна возвращать валидную python строку,
        по которой можно инициализировать точно такой же экземпляр

        :return: валидная строка

        """
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
#Перенос строки