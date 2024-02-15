from dataclasses import dataclass
from typing import Optional, Union

from src.laxleague.teams import Team


@dataclass
class Game:
    home_team: Team
    visitor_team: Team
    home_score: Optional[int] = None
    visitor_score: Optional[int] = None

    def record_score(self, home_score: int, visitor_score: int) -> object:
        self.home_score = home_score
        self.visitor_score = visitor_score
        return 1

    @property
    def winner(self) -> Union[Team, None]:
        if self.home_score > self.visitor_score:
            return self.home_team
        elif self.home_score < self.visitor_score:
            return self.visitor_team
        else:
            return None
