from random import choice, randint

import pytest

from laxleague.games import Game
from laxleague.players import Player
from laxleague.teams import Team

FIRST_NAMES = (
    'player_one', 'Sue', 'Aja', 'Li', 'Barb', 'Emma', 'Sam', 'Jala',
    'Nicole', 'Tatiana', 'Hanna', 'Alison', 'Delanie', 'Nia',
    'Lexi', 'Ellen', 'Molly', 'Ava', 'Abby', 'Heidi', 'Madison',
)

LAST_NAMES = (
    'Smith', 'Jones', 'Baker', 'Frazier', 'Billings', 'Hernandez',
    'Washington', 'Melendez', 'Cho',
)


def get_random_player():
    first = choice(FIRST_NAMES)
    last = choice(LAST_NAMES)
    jersey = randint(0, 9999)
    return Player(
        first_name=first, last_name=last, jersey=jersey
    )


@pytest.fixture
def player_one() -> Player:
    """ Return a sample player *player_one Smith #10* """
    yield Player(first_name='player_one', last_name='Smith', jersey=10)


@pytest.fixture
def team_empty(player_one):
    yield Team('empty')


@pytest.fixture(name='green')
def team_with_defaults(player_one):
    # Make a team with 20 players, with one of them known
    team = Team(name='green')
    team.add_player(player_one)
    for i in range(19):
        team.add_player(get_random_player())

    yield team


@pytest.fixture(name='blue')
def another_team():
    # Make a team with 20 players
    team = Team(name='blue')
    for i in range(20):
        team.add_player(get_random_player())

    yield team


@pytest.fixture
def game_blue_at_green(green, blue):
    # Green is home, Blue is visitor
    yield Game(home_team=green, visitor_team=blue)


@pytest.fixture
def game_type():
    return Game
