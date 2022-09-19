import pytest

from src.v2.cpf import validate_cpf


def test_valid_cpf():
    _valid_cpf = '291.524.122-88'
    assert validate_cpf(_valid_cpf)


def test_same_caracter_in_cpf():
    _same_caracter_cpf = '000.000.000-00'
    _error_expected = 'CPF is the same caractere in all digits'
    with pytest.raises(Exception) as e:
        validate_cpf(_same_caracter_cpf)
    assert _error_expected == str(e.value)


def test_cpf_with_zero_digits():
    _cpf = '62105348300'
    assert validate_cpf(_cpf)


def test_cpf_with_invalid_digits():
    _invalid_cpf = '291.524.12X-XX'
    _error_expected = "invalid literal for int() with base 10: 'X'"
    with pytest.raises(Exception) as e:
        validate_cpf(_invalid_cpf)
    assert _error_expected == str(e.value)


def test_cpf_without_all_digits():
    _invalid_cpf = '2'
    _error_expected = 'CPF incomplete digits'
    with pytest.raises(Exception) as e:
        validate_cpf(_invalid_cpf)
    assert _error_expected == str(e.value)


def test_cpf_none():
    _invalid_cpf = None
    _error_expected = 'CPF is None or Empty'
    with pytest.raises(Exception) as e:
        validate_cpf(_invalid_cpf)
    assert _error_expected == str(e.value)


def test_cpf_empty():
    _invalid_cpf = ''
    _error_expected = 'CPF is None or Empty'
    with pytest.raises(Exception) as e:
        validate_cpf(_invalid_cpf)
    assert _error_expected == str(e.value)


def test_not_create_order_with_invalid_cpf():
    ...


def test_create_order_with_three_items():
    ...


def create_order_with_discount_cupon():
    ...
