from dataclasses import dataclass


@dataclass
class Player:
    first_name: str
    last_name: str
    dob: str

    def __post_init__(self):
        ln = self.last_name.lower()
        fn = self.first_name.lower()
        self.id = f'{ln}-{fn}-{self.dob}'
