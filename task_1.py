class Vehicle:
    """Базовый класс 'Транспортное средство'."""

    def __init__(self, brand: str, model: str, max_speed: float):
        """
        :param brand: Бренд (марка) транспортного средства.
        :param model: Модель транспортного средства.
        :param max_speed: Максимальная скорость в км/ч.
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой.")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой.")
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом.")

        self._brand = brand  # Инкапсуляция: защищенный атрибут, так как бренд редко изменяется.
        self._model = model  # Инкапсуляция: защищенный атрибут.
        self._max_speed = max_speed

    def __str__(self) -> str:
        return f"{self._brand} {self._model}, макс. скорость: {self._max_speed} км/ч"

    def __repr__(self) -> str:
        return f"Vehicle(brand={self._brand!r}, model={self._model!r}, max_speed={self._max_speed!r})"

    def move(self) -> str:
        return f"{self._brand} {self._model} движется со скоростью до {self._max_speed} км/ч."


class Car(Vehicle):
    """Дочерний класс 'Легковой автомобиль'."""

    def __init__(self, brand: str, model: str, max_speed: float, num_doors: int):
        """
        :param brand: Бренд автомобиля.
        :param model: Модель автомобиля.
        :param max_speed: Максимальная скорость автомобиля.
        :param num_doors: Количество дверей.
        """
        super().__init__(brand, model, max_speed)

        if not isinstance(num_doors, int) or num_doors <= 0:
            raise ValueError("Количество дверей должно быть положительным целым числом.")

        self._num_doors = num_doors  # Инкапсуляция: защищенный атрибут.

    def __str__(self) -> str:
        """Перегруженный метод строкового представления."""
        return f"Легковой автомобиль: {self._brand} {self._model}, {self._num_doors} двери, макс. скорость: {self._max_speed} км/ч"

    def __repr__(self) -> str:
        """Перегруженный метод строкового представления для воссоздания объекта."""
        return f"Car(brand={self._brand!r}, model={self._model!r}, max_speed={self._max_speed!r}, num_doors={self._num_doors!r})"

    def move(self) -> str:
        """Унаследованный метод."""
        return super().move() + " Это легковой автомобиль."

    def honk(self) -> str:
        """
        Метод для сигнала автомобиля.

        Причина перегрузки: у автомобилей есть звуковой сигнал, в отличие от других транспортных средств.

        :return: Звуковой сигнал.
        """
        return f"{self._brand} {self._model}: Бииип!"


class Truck(Vehicle):
    """Дочерний класс 'Грузовик'."""

    def __init__(self, brand: str, model: str, max_speed: float, max_load: float):
        """
        :param brand: Бренд грузовика.
        :param model: Модель грузовика.
        :param max_speed: Максимальная скорость грузовика.
        :param max_load: Максимальная грузоподъемность (тонны).
        """
        super().__init__(brand, model, max_speed)

        if not isinstance(max_load, (int, float)) or max_load <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом.")

        self._max_load = max_load  # Инкапсуляция: защищенный атрибут.

    def __str__(self) -> str:
        """Перегруженный метод строкового представления."""
        return f"Грузовик: {self._brand} {self._model}, макс. грузоподъемность: {self._max_load} т, макс. скорость: {self._max_speed} км/ч"

    def __repr__(self) -> str:
        """Перегруженный метод строкового представления для воссоздания объекта."""
        return f"Truck(brand={self._brand!r}, model={self._model!r}, max_speed={self._max_speed!r}, max_load={self._max_load!r})"

    def move(self) -> str:
        """Унаследованный метод с перегрузкой."""
        return f"{self._brand} {self._model} перевозит груз и движется со скоростью до {self._max_speed} км/ч."

    def load_cargo(self, weight: float) -> str:
        """
        Метод для загрузки груза в грузовик.

        Причина перегрузки: у грузовиков есть возможность перевозки груза, в отличие от других транспортных средств.

        :param weight: Вес груза в тоннах.
        :return: Информация о загрузке.
        """
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Вес груза должен быть положительным числом.")
        if weight > self._max_load:
            return f"{self._brand} {self._model}: Слишком тяжелый груз! Максимально допустимо {self._max_load} т."
        return f"{self._brand} {self._model}: Груз {weight} т загружен."


if __name__ == "__main__":
    # Тестирование классов
    car = Car("Honda", "Accord", 220, 4)
    truck = Truck("Isuzu", "Forward", 120, 20)

    print(car)  # Легковой автомобиль
    print(truck)  # Грузовик

    print(car.move())  # Движение легкового авто
    print(truck.move())  # Движение грузовика

    print(car.honk())  # Сигнал автомобиля
    print(truck.load_cargo(15))  # Загрузка груза
    print(truck.load_cargo(25))  # Превышение груза
pass

