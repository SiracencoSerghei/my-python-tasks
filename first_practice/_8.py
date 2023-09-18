def game(terra, power):
    for sublist in terra:
        for energy in sublist:
            if power >= energy:
                power += energy
            else:
                break
    print(power)
    return power

game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1)