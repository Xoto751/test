# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union

class Steel:
    def __init__(self, Sort: Union[int], Width: Union[int]):
        """
        Создание и подготовка к работе объекта "Сталь"

        :param Sort: Марка стали
        :param Width: Толщина пластины

        Примеры:
        >>> steel = Steel(245, 10)  # инициализация экземпляра класса
        """
        if not isinstance(Sort, (int)):
            raise TypeError("Марка стали должна быть типа int")
        if not Sort in [235, 245, 255, 275, 285, 345, 375, 390, 440, 590]:
            raise ValueError("Для ГОСТ 19903-2015 данная марка стали не предусмотрена")
        self.Sort = Sort

        if not isinstance(Width, (int)):
            raise TypeError("Толщина пластины должна быть типа int")
        if not Width in [1, 2, 3, 4, 6, 8, 10, 12, 16, 20]:
            raise ValueError("Проката данной толщины нет в наличии на металлобазе")
        self.Width = Width

    def is_sort_popular(self) -> bool:
        """
        Функция которая проверяет является ли марка и толщина стали ходовой (наиболее популярной для закупки)

        :return: Является ли марка и толщина стали ходовой

        Примеры:
        >>> steel = Steel(390, 3)
        >>> steel.is_sort_popular()
        """

    def increase_thickness(self, inc_: int) -> None:
        """
        Увеличение толщины пластины.
        :param inc_: Добавляемая толщина

        :raise ValueError: Если итоговая толщина вне сортамента на металлобазе, то вызываем ошибку

        Примеры:
        >>> steel = Steel(245, 8)
        >>> steel.increase_thickness(2)
        """
        ...

        if not isinstance(inc_, (int)):
            raise TypeError("Добавляемая толщина должна быть типа int")
        if inc_ < 0:
            raise ValueError("Добавляемая толщина должна положительным числом")


class H_Beam:
    def __init__(self, GOST: Union[str], Number: Union[int]):
        """
        Создание и подготовка к работе объекта "Двутавр"

        :param GOST: Номер двутавра
        :param Number: Номер двутавра

        Примеры:
        >>> h_beam = H_Beam("ГОСТ 8239-89", 40)  # инициализация экземпляра класса
        """
        if not isinstance(GOST, (str)):
            raise TypeError("ГОСТ должен быть типа str")
        if not GOST in ["ГОСТ Р 57837-2017", "ГОСТ 8239-89", "ГОСТ 26020-83"]:
            raise ValueError("Двутавра по данному ГОСТ нет на металлобазе")
        self.GOST = GOST

        if not isinstance(Number, (int)):
            raise TypeError("Номер двутавра должен быть типа int")
        if not Number in [10, 12, 13, 14, 15, 16, 18, 20, 22, 24, 25, 27, 30, 32, 33, 35, 36, 40, 45, 50, 53, 55, 60, 70, 80, 85, 90, 100]:
            raise ValueError("Двутавра данного номера нет на металлобазе")
        self.Number = Number

    def is_gost_popular(self) -> bool:
        """
        Функция которая проверяет является ли двутавр по данному ГОСТ ходовым (наиболее популярным для закупки)

        :return: Является ли двутавр по данному ГОСТ ходовым

        Примеры:moment of resistance
        >>> h_beam = H_Beam("ГОСТ Р 57837-2017", 32)
        >>> h_beam.is_gost_popular()
        """

    def moment_resistance(self) -> float:
        """
        Функция которая вычисляет момент сопротивления двутавра

        :return: Момент сопротивления двутавра

        Примеры:
        >>> h_beam = H_Beam("ГОСТ 26020-83", 53)
        >>> h_beam.moment_resistance()
        """


assortment = [                                      #Инициализация сортамента для работы с классом L_Beam
            {'width_': 20, 'thickness_': [3, 4]},
            {'width_': 25, 'thickness_': [3, 4]},
            {'width_': 28, 'thickness_': [3]},
            {'width_': 30, 'thickness_': [3, 4]},
            {'width_': 32, 'thickness_': [3, 4]},
            {'width_': 35, 'thickness_': [3, 4, 5]},
            {'width_': 40, 'thickness_': [3, 4, 5]},
            {'width_': 45, 'thickness_': [3, 4, 5]},
            {'width_': 50, 'thickness_': [3, 4, 5, 6]},
            {'width_': 56, 'thickness_': [4, 5]},
            {'width_': 63, 'thickness_': [4, 5, 6]},
            {'width_': 70, 'thickness_': [4.5, 5, 6, 7, 8]},
            {'width_': 75, 'thickness_': [5, 6, 7, 8, 9]},
            {'width_': 80, 'thickness_': [5.5, 6, 7, 8]},
            {'width_': 90, 'thickness_': [6, 7, 8, 9]},
            {'width_': 100, 'thickness_': [6.5, 7, 8, 10, 12, 14, 16]},
            {'width_': 110, 'thickness_': [7, 8]},
            {'width_': 125, 'thickness_': [8, 9, 10, 12, 14, 16]},
            {'width_': 140, 'thickness_': [9, 10, 12]},
            {'width_': 160, 'thickness_': [10, 11, 12, 14, 16, 18, 20]},
            {'width_': 180, 'thickness_': [11, 12]},
            {'width_': 200, 'thickness_': [12, 13, 14, 16, 20, 25, 30]},
            {'width_': 220, 'thickness_': [14, 16]},
            {'width_': 250, 'thickness_': [16, 18, 20, 22, 25, 28, 30, 35]}
        ]

class L_Beam:
    def __init__(self, Width: Union[int], Thickness: Union[int, float]):

        """
        Создание и подготовка к работе объекта "Уголок"
        Создание списка сортамента

        :param Width: Ширина полки
        :param Thickness: Толщина полки

        Примеры:
        >>> l_beam = L_Beam(50, 5)  # инициализация экземпляра класса
        """

        if not isinstance(Width, (int)):
            raise TypeError("Ширина полки должна быть типа int")
        for result, dic_ in enumerate(assortment):
            if dic_.get('width_', '') == Width:
                break;
        else:
            result = None
        if result == None:
            raise ValueError("Данная ширина полки не предусмотрена ГОСТ 8509-93")

        if not isinstance(Thickness, (int, float)):
            raise TypeError("Толщина полки должна быть типа int или float")
        if not Thickness in dic_.get('thickness_') and not result == None:
            raise ValueError("Данная толщина полки для данной ширины полки не предусмотрена ГОСТ 8509-93")

    def moment_of_inertia(self) -> float:
        """
        Функция которая вычисляет момент инерции для выбранного сечения

        :return: Момент инерции уголка

        Примеры:
        >>> l_beam = L_Beam(100, 10)
        >>> l_beam.moment_of_inertia()
        """

    def weight(self) -> float:
        """
        Функция которая вычисляет удельную массу (массу на 1 погонный метр) выбранного сечения

        :return: Удельная масса

        Примеры:
        >>> l_beam = L_Beam(250, 20)
        >>> l_beam.moment_of_inertia()
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
