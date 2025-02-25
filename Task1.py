class Vehicle:
    """ Базовый класс для транспортных средств. """

    def __init__(self, make: str, model: str, year: int):
        """
        Конструктор для инициализации транспортного средства.

        :param make: Производитель транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self._make = make  # Непубличный атрибут, чтобы предотвратить случайные изменения
        self._model = model  # Непубличный атрибут, чтобы предотвратить случайные изменения
        self._year = year  # Непубличный атрибут, чтобы предотвратить случайные изменения

    @property
    def make(self) -> str:
        """ Возвращает производителя транспортного средства. """
        return self._make

    @property
    def model(self) -> str:
        """ Возвращает модель транспортного средства. """
        return self._model

    @property
    def year(self) -> int:
        """ Возвращает год выпуска транспортного средства. """
        return self._year

    def start_engine(self) -> str:
        """ Запускает двигатель транспортного средства. """
        return f"Двигатель {self.make} {self.model} запущен."

    def __str__(self) -> str:
        """ Возвращает строковое представление транспортного средства. """
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """ Возвращает официальное строковое представление транспортного средства. """
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r})"


class Car(Vehicle):
    """ Класс для легкового автомобиля. """

    def __init__(self, make: str, model: str, year: int, doors: int):
        """
        Конструктор для инициализации легкового автомобиля.

        :param make: Производитель легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей в легковом автомобиле.
        """
        super().__init__(make, model, year)  # Вызов конструктора базового класса
        self._doors = doors  # Непубличный атрибут, чтобы предотвратить случайные изменения

    @property
    def doors(self) -> int:
        """ Возвращает количество дверей в легковом автомобиле. """
        return self._doors

    def start_engine(self) -> str:
        """ Запускает двигатель легкового автомобиля. """
        return f"Легковой автомобиль {self.make} {self.model} с {self.doors} дверями запущен."

    def __str__(self) -> str:
        """ Возвращает строковое представление легкового автомобиля. """
        return f"{super().__str__()} с {self.doors} дверями"

    def __repr__(self) -> str:
        """ Возвращает официальное строковое представление легкового автомобиля. """
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r}, doors={self.doors!r})"


class Truck(Vehicle):
    """ Класс для грузового автомобиля. """

    def __init__(self, make: str, model: str, year: int, payload_capacity: float):
        """
        Конструктор для инициализации грузового автомобиля.

        :param make: Производитель грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param payload_capacity: Грузоподъемность грузового автомобиля в тоннах.
        """
        super().__init__(make, model, year)  # Вызов конструктора базового класса
        self._payload_capacity = payload_capacity  # Непубличный атрибут, чтобы предотвратить случайные изменения

    @property
    def payload_capacity(self) -> float:
        """ Возвращает грузоподъемность грузового автомобиля. """
        return self._payload_capacity

    def start_engine(self) -> str:
        """ Запускает двигатель грузового автомобиля. """
        return f"Грузовой автомобиль {self.make} {self.model} с грузоподъемностью {self.payload_capacity} тонн запущен."


if __name__ == '__main__':
    car = Car("volvo", "s40", 2004, 5)
    print(car.__str__())
    print(car.__repr__())