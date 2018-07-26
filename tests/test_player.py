from laxleague.players import Player


def test_constructor():
    p = Player(first_name='Mary', last_name='Smith', dob='2005/01/01')
    assert 'Mary' == p.first_name
    assert 'Smith' == p.last_name
    assert 'smith-mary-2005/01/01' == p.id