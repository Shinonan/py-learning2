import doctest
from abc import ABC


class Vehicle(ABC):
    """Абстрактный класс Транспортное средство"""

    def __init__(self, brand: str, max_speed: float):
        """
        Создание и подготовка к работе объекта "Транспортное средство"

        :param brand: Марка транспортного средства
        :param max_speed: Максимальная скорость (км/ч)

        Примеры:
        >>> car = Car("Toyota", 180, 4)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть строкой")
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")

        self._brand = brand
        self._max_speed = max_speed

    def get_brand(self) -> str:
        """Возвращает марку транспортного средства"""
        return self._brand

    def get_max_speed(self) -> float:
        """Возвращает максимальную скорость"""
        return self._max_speed

    def move(self) -> None:
        """Абстрактный метод для передвижения транспортного средства"""
        raise NotImplementedError("Метод move() должен быть переопределен в подклассе")


class Car(Vehicle):
    """Класс Автомобиль"""

    def __init__(self, brand: str, max_speed: float, doors: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param max_speed: Максимальная скорость
        :param doors: Количество дверей

        Примеры:
        >>> car = Car("Toyota", 180, 4)
        """
        super().__init__(brand, max_speed)

        if not isinstance(doors, int) or doors <= 0:
            raise ValueError("Количество дверей должно быть положительным числом")

        self._doors = doors

    def move(self) -> None:
        """Реализация метода движения автомобиля"""
        print(f"{self.get_brand()} едет со скоростью {self.get_max_speed()} км/ч")


class Tree(ABC):
    """Абстрактный класс Дерево"""

    def __init__(self, species: str, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param age: Возраст дерева (в годах)

        Примеры:
        >>> oak = Oak("Дуб", 50)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом")

        self._species = species
        self._age = age

    def get_species(self) -> str:
        """Возвращает вид дерева"""
        return self._species

    def get_age(self) -> int:
        """Возвращает возраст дерева"""
        return self._age

    def photosynthesize(self) -> None:
        """Абстрактный метод для фотосинтеза"""
        raise NotImplementedError("Метод photosynthesize() должен быть переопределен в подклассе")


class Oak(Tree):
    """Класс Дуб"""

    def photosynthesize(self) -> None:
        """Реализация метода фотосинтеза"""
        print(f"{self.get_species()} поглощает солнечный свет и производит кислород")


class SocialNetwork(ABC):
    """Абстрактный класс Социальная сеть"""

    def __init__(self, name: str, users: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название соцсети
        :param users: Количество пользователей

        Примеры:
        >>> fb = Facebook("Facebook", 2900000000)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(users, int) or users < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным числом")

        self._name = name
        self._users = users

    def get_name(self) -> str:
        """Возвращает название соцсети"""
        return self._name

    def get_users(self) -> int:
        """Возвращает количество пользователей"""
        return self._users

    def post_content(self, content: str) -> None:
        """Абстрактный метод для публикации контента"""
        raise NotImplementedError("Метод post_content() должен быть переопределен в подклассе")


class Facebook(SocialNetwork):
    """Класс Facebook"""

    def post_content(self, content: str) -> None:
        """Реализация метода публикации контента"""
        print(f"Пост в {self.get_name()}: {content}")


if __name__ == "__main__":
    doctest.testmod()
