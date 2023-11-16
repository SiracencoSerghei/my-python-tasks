from ex03 import Game, Gamer

g1 = Game("Doom")
g2 = Game("CS:Go")
g3 = Game("HeroesIII")

gamer = Gamer("Bill")

for g in (g1, g2, g3):
    gamer.add_game(g)

print(gamer.games)
print(gamer.play_game("Doom"))
print(gamer.games)
