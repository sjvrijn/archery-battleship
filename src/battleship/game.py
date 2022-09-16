"""Play a game of Battleship"""

from itertools import count

from battleship.board import Board
from battleship.ship import ShipPartState


def play_1p_game():
    """Play a '1p' game: place the boats and sink them in the fewest moves"""
    b = Board()
    print("what fleet should be placed?")
    fleet_str = input()
    fleet = map(int, fleet_str.strip('\n').split(','))
    b.place_random_fleet(fleet)

    num_sunk = 0
    for move in count(1):
        print(b.display(public=True))

        coord = input('Where do you shoot? [A0 ... J9] ')
        row, col = ord(coord[0])-65, int(coord[1])
        if row > 10:
            row -= 32  # a..j instead of A..J
        result = b.shoot(row, col)
        if result == ShipPartState.SUNK:
            num_sunk += 1
            print(f"Another ship sunk, {n-num_sunk} left.")

        if b.fleet_sunk():
            print(f"Victory! Fleet sunk in {move} moves")
            break


if __name__ == "__main__":
    play_1p_game()
