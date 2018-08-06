from pytest_bdd import scenario, given, when, then, parsers

from laxleague.games import Game
from laxleague.teams import Team


@scenario('games.feature', 'Determine The Winner')
def test_games_feature():
    pass


@given('a home team of Blue')
def blue():
    return Team('Blue')


@given('a visiting team of Red')
def red():
    return Team('Red')


@given('a game between them')
def game_red_blue(blue, red):
    return Game(home_team=blue, visitor_team=red)


@when(parsers.parse('the score is {home:d} for Blue to {visitor:d} for Red'))
def record_score(game_red_blue, home, visitor):
    game_red_blue.record_score(home, visitor)


@then('Blue is the winner')
def winner(game_red_blue):
    assert 'Blue' == game_red_blue.winner.name
