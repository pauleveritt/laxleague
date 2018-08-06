from pytest_bdd import scenario, given, when, then

from laxleague.games import Game
from laxleague.teams import Team


@scenario('games.feature', 'Determine The Winner')
def test_games_feature(game_red_blue, blue):
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


@when('the score is 10 for Blue to 5 for Red')
def record_score(game_red_blue):
    game_red_blue.record_score(10, 5)


@then('Blue is the winner')
def winner(game_red_blue):
    assert 'Blue' == game_red_blue.winner.name
