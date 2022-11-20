from player import Player
from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, reader: "PlayerReader") -> None:
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        nat_players = filter(lambda p: p.nationality == nationality, players)
        return sorted(nat_players, key= lambda p: p.goals + p.assists, reverse=True)
