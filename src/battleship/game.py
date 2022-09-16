"""Play a game of Battleship"""

from itertools import count

from battleship.board import Board
from battleship.ship import ShipPartState


def play_1p_game():
    """Play a '1p' game: sink a randomly placed fleet in the fewest moves"""
    b = Board()
    print("what fleet should be placed? (leave empty for default)")
    fleet_str = input()
    if fleet_str:
        fleet = list(map(int, fleet_str.strip('\n').split(',')))
        b.place_random_fleet(fleet)
    else:
        b.place_random_fleet()

    for move in count(1):
        print(b.display(public=True))

        coord = input('Where do you shoot? [A0 ... J9] ')
        row, col = ord(coord[0])-65, int(coord[1])
        if row > 10:
            row -= 32  # a..j instead of A..J
        result = b.shoot(row, col)
        if result == ShipPartState.SUNK:
            num_sunk = sum(s.sunk for s in b.ships)
            print(f"Another ship sunk, {len(b.ships)-num_sunk} left.")

        if b.fleet_sunk():
            print(f"Victory! Fleet sunk in {move} moves")
            print(b.display(public=True))
            break


if __name__ == "__main__":
    play_1p_game()
