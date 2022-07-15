
from dataclasses import dataclass
from operator import attrgetter
from typing import Callable, Sequence

@dataclass
class Item:
    name: str
    price: int

@dataclass
class SpecialOffer:
    predicates: Sequence[Sequence[Callable]]


ITEMS = {
    "A": Item(name="A", price=50),
    "B": Item(name="B", price=30),
    "C": Item(name="C", price=20),
    "D": Item(name="D", price=15),
}

SPECIAL_OFFERS = [
    SpecialOffer(predicates=[[lambda item: item.name == "A"] * 3])
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        items = [ITEMS[sku] for sku in skus]
    except KeyError:
        return -1

    return sum(map(attrgetter("price"), items))

if __name__ == "__main__":
    print(checkout("AAAA"))

