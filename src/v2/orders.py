from dataclasses import dataclass
from decimal import Decimal

from src.v2.cpf import validate_cpf


@dataclass
class Items:
    """Represent one item"""

    _id: int
    price: Decimal
    name: str


@dataclass
class Order:
    """Represent one order"""

    user_cpf: str
    items: list[Items]
    total: Decimal


def _calculate_total_price(items: list[Items]) -> Decimal:
    total_price = 0.0
    for item in items:
        total_price = total_price + item.price
    return total_price


def _calculate_total_price_with_disconts(
    total: Decimal, cupon: Decimal
) -> Decimal:
    discont = total * cupon
    return total - discont


def create_order(cpf: str, items: list[Items], cupon: Decimal = 0) -> Order:
    if not validate_cpf(cpf):
        raise Exception('CPF is not valid!')
    total = _calculate_total_price(items)
    total = _calculate_total_price_with_disconts(total, cupon)
    return Order(user_cpf=cpf, total=total, items=items)
