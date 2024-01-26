from dataclasses import dataclass
from typing import Optional

@dataclass
class Address:
    first_name: str
    last_name: str
    company: Optional[str]
    address_line_1: str
    address_line_2: Optional[str]
    city: str
    state: str
    country: str
    zipcode: str
    phone: str
    