from dataclasses import dataclass, field
from typing import Dict

from laxleague.players import Player


class Teams:
    pass


def make_players():
    return {}


@dataclass
class Team:
    name: str
    players: Dict[str, Player] = field(default_factory=make_players)

    def add_player(self, player: Player):
        self.players[player.id] = player
