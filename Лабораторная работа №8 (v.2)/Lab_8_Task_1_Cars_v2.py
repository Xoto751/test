class Car:
    """
    Базовый класс для представления автомобиля.

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
        mileage (float): Пробег автомобиля в километрах.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float):
        """
        Конструктор класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param mileage: Пробег автомобиля в километрах.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        :return: Строка с описанием автомобиля.
        """
        return f"{self.brand} {self.model} ({self.year}), пробег: {self.mileage} км"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление автомобиля.

        :return: Формальное строковое представление.
        """
        return f"Car(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, mileage={self.mileage!r})"

    def increase_mileage(self, distance: float) -> None:
        """
        Увеличивает пробег автомобиля на заданное расстояние.

        :param distance: Расстояние в километрах, на которое нужно увеличить пробег.
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным.")
        self.mileage += distance


class PassengerCar(Car):
    """
    Дочерний класс для представления легкового автомобиля.

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
        mileage (float): Пробег автомобиля в километрах.
        body_type (str): Тип кузова легкового автомобиля.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float, body_type: str):
        """
        Конструктор класса PassengerCar.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param mileage: Пробег автомобиля в километрах.
        :param body_type: Тип кузова легкового автомобиля.
        """
        super().__init__(brand, model, year, mileage)
        self.body_type = body_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        :return: Строка с описанием легкового автомобиля.
        """
        return f"{super().__str__()}, тип кузова: {self.body_type}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление легкового автомобиля.

        :return: Формальное строковое представление.
        """
        return f"PassengerCar(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, mileage={self.mileage!r}, body_type={self.body_type!r})"

    def increase_mileage(self, distance: float) -> None:
        """
        Увеличивает пробег автомобиля на заданное расстояние.
        Перегруженный метод, который также выводит сообщение о том, что пробег увеличен.

        :param distance: Расстояние в километрах, на которое нужно увеличить пробег.
        """
        super().increase_mileage(distance)
        print(f"Пробег легкового автомобиля {self.brand} {self.model} ({self.year}) увеличен на {distance} км.")


class Truck(Car):
    """
    Дочерний класс для представления грузового автомобиля.

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
        mileage (float): Пробег автомобиля в километрах.
        load_capacity (float): Грузоподъемность автомобиля в тоннах.
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float, load_capacity: float):
        """
        Конструктор класса Truck.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param mileage: Пробег автомобиля в километрах.
        :param load_capacity: Грузоподъемность автомобиля в тоннах.
        """
        super().__init__(brand, model, year, mileage)
        self.load_capacity = load_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        :return: Строка с описанием грузового автомобиля.
        """
        return f"{super().__str__()}, грузоподъемность: {self.load_capacity} т"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление грузового автомобиля.

        :return: Формальное строковое представление.
        """
        return f"Truck(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, mileage={self.mileage!r}, load_capacity={self.load_capacity!r})"

    def increase_mileage(self, distance: float) -> None:
        """
        Увеличивает пробег автомобиля на заданное расстояние.
        Перегруженный метод, который также выводит сообщение о том, что пробег увеличен.

        :param distance: Расстояние в километрах, на которое нужно увеличить пробег.
        """
        super().increase_mileage(distance)
        print(f"Пробег грузового автомобиля {self.brand} {self.model} ({self.year}) увеличен на {distance} км.")


if __name__ == "__main__":
    # Создаем объекты классов
    passenger_car = PassengerCar("Toyota", "Corolla", 2020, 15000.5, "седан")
    truck = Truck("Volvo", "FH16", 2018, 75000.0, 20.0)

    # Выводим информацию об автомобилях
    print(passenger_car)
    print(truck)

    # Увеличиваем пробег
    passenger_car.increase_mileage(100.0)
    truck.increase_mileage(200.0)

    # Выводим обновленную информацию
    print(passenger_car)
    print(truck)