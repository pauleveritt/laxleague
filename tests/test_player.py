from laxleague.players import Player


def test_constructor():
    p = Player(first_name='Jane', last_name='Jones', jersey=11)
    assert 'Jane' == p.first_name
    assert 'Jones' == p.last_name
    assert 'jones-jane-11' == p.id


def test_another_player(player_one):
    assert 'player_one' == player_one.first_name
