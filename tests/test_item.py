import pytest
from src.item import Item


@pytest.fixture
def testing_item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(testing_item):
    """проверяем итоговую сумму при заданных параметрах товара"""
    assert testing_item.calculate_total_price() == 200000


def test_apply_discount(testing_item):
    """Проверяем применение скидки с учетом изменения процента"""
    Item.pay_rate = 0.5
    testing_item.apply_discount()
    assert testing_item.price == 5000


def test_self_name(testing_item):
    assert testing_item.name == 'Смартфон'
    testing_item.name = 'Телефон'
    assert testing_item.name == 'Телефон'


def test_len_name(testing_item):
    assert len(testing_item.name) <= 10
