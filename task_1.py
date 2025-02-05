class Book:

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def get_name(self) -> str:
        return self._name

    def get_author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга '{self.get_name()}'. Автор: {self.get_author()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r})"


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.set_pages(pages)

    def get_pages(self) -> int:
        return self._pages

    def set_pages(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError()
        self._pages = value

    def __str__(self) -> str:
        return f"Бумажная книга '{self.get_name()}'. Автор: {self.get_author()}, страниц: {self.get_pages()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}, pages={self.get_pages()})"


class AudioBook(Book):

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.set_duration(duration)

    def get_duration(self) -> float:
        return self._duration

    def set_duration(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError()
        self._duration = float(value)

    def __str__(self) -> str:
        return f"Аудиокнига '{self.get_name()}'. Автор: {self.get_author()}, продолжительность: {self.get_duration()} часов"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.get_name()!r} , author={self.get_author()!r} , duration={self.get_duration()})"
