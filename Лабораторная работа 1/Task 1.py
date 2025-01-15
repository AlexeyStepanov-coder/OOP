# TODO Написать 3 класса с документацией и аннотацией типов
class Table:
    def __init__(self, material: str, length: float, width: float):
        """
        Инициализация стола.

        :param material: Материал стола (например, дерево, металл).
        :param length: Длина стола в сантиметрах (должна быть больше 0).
        :param width: Ширина стола в сантиметрах (должна быть больше 0).
        :raises ValueError: Если length или width меньше или равен 0.
        """
        if length <= 0:
            raise ValueError("Длина должна быть больше 0.")
        if width <= 0:
            raise ValueError("Ширина должна быть больше 0.")

        self.material = material
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        """
        Вычисляет площадь стола.

        :return: Площадь стола.
        :rtype: float
        :doctest:
        >>> table = Table("дерево", 200, 100)
        >>> table.calculate_area()
        20000
        """
        return self.length * self.width

    def describe(self) -> str:
        """
        Возвращает описание стола.

        :return: Описание стола.
        :rtype: str
        :doctest:
        >>> table = Table("металл", 150, 75)
        >>> table.describe()
        'Стол из металл размером 150x75 см.'
        """
        return f"Стол из {self.material} размером {self.length}x{self.width} см."

class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Инициализация дерева.

        :param species: Вид дерева (например, сосна, дуб).
        :param height: Высота дерева в метрах (должна быть больше 0).
        :param age: Возраст дерева в годах (должен быть неотрицательным).
        :raises ValueError: Если height меньше или равен 0 или age отрицателен.
        """
        if height <= 0:
            raise ValueError("Высота должна быть больше 0.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")

        self.species = species
        self.height = height
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева на заданное количество лет.

        :param years: Количество лет, на которое нужно увеличить возраст.
        :type years: int
        :raises ValueError: Если years отрицательно.
        :doctest:
        >>> tree = Tree("сосна", 10, 5)
        >>> tree.grow(3)
        >>> tree.age
        8
        """
        if years < 0:
            raise ValueError("Количество лет для роста не может быть отрицательным.")
        self.age += years

    def describe(self) -> str:
        """
        Возвращает описание дерева.

        :return: Описание дерева.
        :rtype: str
        :doctest:
        >>> tree = Tree("дуб", 15, 20)
        >>> tree.describe()
        'дуб высотой 15 метров, возраст 20 лет.'
        """
        return f"{self.species} высотой {self.height} метров, возраст {self.age} лет."
class SocialMedia:
    def __init__(self, name: str, user_count: int, launch_year: int):
        """
        Инициализация социальной сети.

        :param name: Название социальной сети.
        :param user_count: Количество пользователей (должно быть неотрицательным).
        :param launch_year: Год запуска социальной сети (должен быть не позже текущего года).
        :raises ValueError: Если user_count отрицателен или launch_year позже текущего.
        """
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        from datetime import datetime
        current_year = datetime.now().year
        if launch_year > current_year:
            raise ValueError("Год запуска не может быть в будущем.")

        self.name = name
        self.user_count = user_count
        self.launch_year = launch_year

    def add_user(self) -> None:
        """
        Добавляет одного пользователя к количеству пользователей.

        :raises ValueError: Если user_count достиг максимума.
        :doctest:
        >>> social_media = SocialMedia("Facebook", 1000, 2004)
        >>> social_media.add_user()
        >>> social_media.user_count
        1001
        """
        self.user_count += 1

    def describe(self) -> str:
        """
        Возвращает описание социальной сети.

        :return: Описание социальной сети.
        :rtype: str
        :doctest:
        >>> social_media = SocialMedia("Twitter", 500, 2006)
        >>> social_media.describe()
        'Twitter, запущен в 2006 году, пользователей: 500.'
        """
        return f"{self.name}, запущен в {self.launch_year} году, пользователей: {self.user_count}."


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
