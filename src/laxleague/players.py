from dataclasses import dataclass


@dataclass
class Player:
    first_name: str
    last_name: str
    jersey: int

    def __post_init__(self):
        ln = self.last_name.lower()
        fn = self.first_name.lower()
        self.id = f'{ln}-{fn}-{self.jersey}'


if __name__ == "__main__":
    p = Player(first_name='Jane', last_name='Jones', jersey=11)
    print(f"Hello {p.first_name}")
