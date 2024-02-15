import pytest

from src.laxleague.games import Game


def test_construction(green, blue):
    g = Game(home_team=green, visitor_team=blue)
    assert green == g.home_team
    assert blue == g.visitor_team


def test_add_game(green, blue):
    g = Game(home_team=green, visitor_team=blue)
    g.record_score(home_score=10, visitor_score=5)


@pytest.mark.parametrize(
    'home, visitor, winner',
    [
        (10, 5, 'green'),
        (5, 10, 'blue'),
    ]
)
def test_winner(game_blue_at_green, home, visitor, winner):
    game_blue_at_green.record_score(home_score=home, visitor_score=visitor)
    assert winner == game_blue_at_green.winner.name


def test_tie(game_blue_at_green):
    game_blue_at_green.record_score(home_score=5, visitor_score=5)
    assert None is game_blue_at_green.winner
