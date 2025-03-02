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
    """Класс, представляющий книгу."""

    def __init__(self, id_: int, name: str, pages: int):
        """
        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("ID должен быть положительным целым числом.")
        if not isinstance(name, str) or not name:
            raise ValueError("Название книги должно быть непустой строкой.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name={self.name!r}, pages={self.pages})"


class Library:
    """Класс, представляющий библиотеку."""

    def __init__(self, books: list[Book] = None):
        """
        :param books: Список книг в библиотеке (по умолчанию пустой список).
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий идентификатор книги для добавления в библиотеку.

        :return: ID следующей книги.
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её ID.

        :param book_id: ID книги.
        :raise ValueError: Если книга с указанным ID не найдена.
        :return: Индекс книги в списке.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))
