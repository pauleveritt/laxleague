def test_construction(team_empty):
    assert {} == team_empty.players


def test_with_default_players(green):
    assert 20 == len(green.players)
