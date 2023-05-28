import pytest

from src.phone import Phone


@pytest.fixture
def testing_phone():
    return Phone("Samsung", 20000, 10, 2)


def test_init_num_of_sim(testing_phone):
    """Проверка на установку значения количества сим карт"""
    assert testing_phone.number_of_sim == 2
    testing_phone.number_of_sim = 0
    assert ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
    testing_phone.number_of_sim = 1.5
    assert ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")


def test_str(testing_phone):
    """Тест метода __str__"""
    assert str(testing_phone) == 'Samsung'


def test_repr(testing_phone):
    """Тест метода __repr__"""
    assert repr(testing_phone) == "Phone('Samsung', 20000, 10, 2)"
