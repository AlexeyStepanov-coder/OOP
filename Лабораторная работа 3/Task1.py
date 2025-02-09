class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Бумажный экземпляр """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}. Страниц: {self.pages}"

class AudioBook(Book):
    """ Аудио экземпляр """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        return f"{super().__str__()}. Продолжительность: {self.duration:.2f} часов"

if __name__ == '__main__':
    paper_book = PaperBook("Ересь хоруса", "Дэн Абнетт", 820)
    print(paper_book)
    print(repr(paper_book))

    audio_book = AudioBook("От хорошего к великому", "Джим Коллинз", 9.7)
    print(audio_book)
    print(repr(audio_book))