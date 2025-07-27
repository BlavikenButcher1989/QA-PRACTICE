from faker import Faker
from dataclasses import dataclass

faker_en = Faker('en')

@dataclass
class Generator:
    string: str



def generator():
    yield Generator(
        string=faker_en.pystr(min_chars=2)
    )