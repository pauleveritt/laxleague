from laxleague.players import Player


def test_constructor():
    p = Player(first_name='Mary', last_name='Smith', jersey=11)
    assert 'Mary' == p.first_name
    assert 'Smith' == p.last_name
    assert 'smith-mary-11' == p.id