import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """
        Сеттер для параметра имени name, проверяет условие, что длинна менее 10 символов
        """
        if len(name) > 10:
            print("Длина наименования товара превышает 10 символов")
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """Функция для чтения информации из файла csv по статическому пути к файлу
        при чтении создаются экземпляры класса по ключам name, price, quantity"""
        with open('../src/items.csv', 'r', encoding="cp1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total = self.price * self.quantity
        return total

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @staticmethod
    def string_to_number(value: str):
        """
        Принимает значение в виде строки (str) и возвращает целое число
        """
        value = float(value)
        return int(value)
