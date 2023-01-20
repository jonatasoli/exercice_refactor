import pytest

from src.v2.orders import Items, create_order


def test_not_create_order_with_invalid_cpf():
    _cpf = '291.524.122'
    _items = [Items(name='Item test 1', price=10.0, _id=1)]
    _error_expected = 'CPF is not valid!'
    with pytest.raises(Exception) as err:
        create_order(_cpf, _items)
    assert _error_expected == str(err.value)


def test_create_order_with_three_items():
    _cpf = '291.524.122-88'
    _items = []
    _items.append(Items(name='Item test 1', price=10.0, _id=1))
    _items.append(Items(name='Item test 2', price=20.0, _id=2))
    _items.append(Items(name='Item test 3', price=70.0, _id=3))
    order = create_order(_cpf, _items)
    assert order.total == 100.0
    assert order.user_cpf == _cpf
    assert _items == order.items


def create_order_with_discount_cupon():
    _cpf = '291.524.122-88'
    _items = [Items(name='Item test 1', price=100.0, id=1)]
    _cupon = 80.0
    order = create_order(_cpf, _items, _cupon)
    assert order.total == 20.0
    assert order.user_cpf == _cpf
    assert _items == order.items

def given_expired_cupon_should_not_applied():
    _cpf = '291.524.122-88'
    _items = [Items(name='Item test 1', price=100.0, id=1)]
    _cupon = 80.0
    order = create_order(_cpf, _items, _cupon)
    assert order.total == 20.0
    assert order.user_cpf == _cpf
    assert _items == order.items
