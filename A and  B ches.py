lookup = {".": 0,
          "q": 9, "Q": -9,
          "r": 5, "R": -5,
          "n": 3, "N": -3,
          "b": 3, "B": -3,
          "p": 1, "P": -1,
          "k": 0, "K": -0}
points = sum(map(lookup.__getitem__, open(0).read().replace("\n", "")))
print("White" if points < 0 else "Black" if points else "Draw")