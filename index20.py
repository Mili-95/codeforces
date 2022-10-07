def chess_games(number, winners):
    anton = 0
    danik = 0
    for i in winners:
        if i == 'A':
            anton += 1
        else:
            danik += 1
    if anton > danik:
        return "Anton"
    elif danik > anton:
        return "Danik"
    else:
        return "Friendship"
        _


if __name__ == "__main__":
    number = int(input())
    winners = input()
    print(chess_games(number, winners))
