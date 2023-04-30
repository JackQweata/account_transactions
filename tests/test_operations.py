import pytest

from src.operation import AccountTransactions


def test_get_data(operations):
    assert AccountTransactions(operations).get_date() == '26.08.2019'


@pytest.mark.parametrize("values, expected", [
    (pytest.lazy_fixture('operations'), "Maestro 1596 78** **** 5199"),
    (pytest.lazy_fixture('operations_from'), "")
])
def test_get_from(values, expected):
    account_transactions = AccountTransactions(values)
    assert account_transactions.get_from_operation() == expected


def test_get_to(operations):
    assert AccountTransactions(operations).get_to_operation() == '**9589'
