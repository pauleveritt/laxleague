from src.laxleague.players import Player


def test_constructor():
    p = Player(first_name='Jane', last_name='Smith', jersey=11)
    assert 'Jane' == p.first_name
    assert 'Smith' == p.last_name
    assert 'smith-jane-11' == p.id


def test_another_player(player_one):
    assert 'player_one' == player_one.first_name
