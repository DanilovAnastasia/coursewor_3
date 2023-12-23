from functions import get_only_executed_state, get_sort_by_date, print_trans
from date_by_testing import operations_date_1, operations_date_2


def test_get_only_executed_state():
    assert get_only_executed_state(operations_date_1) == operations_date_1[0:1]
    assert get_only_executed_state(operations_date_2) == []
    assert get_only_executed_state([]) == []


def test_get_sort_by_date():
    assert get_sort_by_date(operations_date_1) == operations_date_1
    assert get_sort_by_date([]) == []


def test_print_trans():
    assert print_trans(operations_date_1[0]) == "03.07.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n8221.37 USD.\n"
