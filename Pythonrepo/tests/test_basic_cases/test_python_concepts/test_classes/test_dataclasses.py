from dataclasses import dataclass
from dataclasses import field

@dataclass
class Person:
    name: str
    age: int
    valid_land_codes: list[str] = field(default_factory=lambda:["+91"])