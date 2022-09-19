from src.v2.cpf import validate_cpf


def test_valid_cpf():
    _valid_cpf = '291.524.122-88'
    assert validate_cpf(_valid_cpf)


def test_same_caracter_in_cpf():
    _same_caracter_cpf = '000.000.000-00'
    assert not validate_cpf(_same_caracter_cpf)


def test_cpf_with_zero_digits():
    _cpf = '62105348300'
    assert validate_cpf(_cpf)


def test_cpf_with_invalid_digits():
    _valid_cpf = '291.524.12X-XX'
    assert not validate_cpf(_valid_cpf)


def test_cpf_without_all_digits():
    _valid_cpf = '2'
    assert not validate_cpf(_valid_cpf)


def test_cpf_none():
    _valid_cpf = None
    assert not validate_cpf(_valid_cpf)


def test_cpf_empty():
    _valid_cpf = ''
    assert not validate_cpf(_valid_cpf)


def test_not_create_order_with_invalid_cpf():
    ...


def test_create_order_with_three_items():
    ...


def create_order_with_discount_cupon():
    ...
