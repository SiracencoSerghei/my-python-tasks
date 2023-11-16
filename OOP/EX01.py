data = {"name": "Bill",
        "games": [
            {"name": "Doom", "counter": 10},
            {"name": "WoW", "counter": 15},
            {"name": "HeroesIII", "counter": 20}]}


class Game:
    def __init__(self, name: str) -> None:
        self.name = name
        self.count = 0

    def play_game(self):
        self.count += 1

    def __repr__(self) -> str:
        return f"{self.name = }, {self.count = }"


class Gamer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.games = []

    def add_game(self, game: Game) -> None:
        self.games.append(game)

    def play_game(self, game_name: str) -> str:
        for g in self.games:
            if g.name == game_name:
                g.play_game()
                return "Good game"
        return "Bad game"


if __name__ == '__main__':
    print(data["games"][0]["counter"])
