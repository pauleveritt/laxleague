from random import choice

import pytest

from laxleague.players import Player
from laxleague.teams import Team

FIRST_NAMES = (
    'Mary', 'Sue', 'Aja', 'Li', 'Barb', 'Emma', 'Sam', 'Jala',
    'Nicole', 'Tatiana', 'Hanna')

LAST_NAMES = (
    'Smith', 'Jones', 'Baker', 'Frazier', 'Billings', 'Hernandez',
    'Washington', 'Melendez', 'Cho'
)

DOBs = (
    '2005/10/01', '2005/09/01', '2006/01/01', '2005/10/02', '2005/10/13',
    '2005/01/01', '2005/02/02', '2005/03/03', '2005/04/04'
)


@pytest.fixture(name='mary')
def player_one():
    yield Player(first_name='Mary', last_name='Smith', dob='2005/01/01')


@pytest.fixture()
def team_empty(mary):
    yield Team('empty')


@pytest.fixture(name='green')
def team_with_defaults(mary):
    # Make a team with 20 players, with one of them known
    team = Team(name='green')
    team.add_player(mary)
    for i in range(19):
        first_name = choice(FIRST_NAMES)
        last_name = choice(LAST_NAMES)
        dob = choice(DOBs)
        player = Player(
            first_name=first_name, last_name=last_name, dob=dob
        )
        team.add_player(player)

    yield team
