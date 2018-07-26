import pytest


def test_construction(team_empty):
    assert {} == team_empty.players


def test_with_default_players(green):
    assert 20 == len(green.players)


def test_exception_on_duplicate(green, mary):
    with pytest.raises(KeyError):
        green.add_player(mary)


