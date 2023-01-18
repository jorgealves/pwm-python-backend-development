from typing import List
from dataclasses import dataclass

@dataclass()
class MenuItem:
    name: str
    price: float


@dataclass()
class Ementa:
    produtos:List[MenuItem]
