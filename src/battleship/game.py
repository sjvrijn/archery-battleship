"""Play a game of Battleship"""

from itertools import count, product
from random import shuffle
from typing import Sequence

from battleship.board import Board
from battleship.ship import ShipPartState


def play_1p_game(fleet: Sequence[int]):
    """Play a '1p' game: sink a randomly placed fleet in the fewest moves"""
    b = Board()
    b.place_random_fleet(fleet)

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

def simulate_random_strategy(fleet: Sequence[int]) -> int:
    """Simulate a randomly played game: shoot all squared once in random order"""
    b = Board()
    b.place_random_fleet(fleet)

    shots = list(product(range(b.size), range(b.size)))
    shuffle(shots)
    for move, (r,c) in enumerate(shots):
        b.shoot(r,c)
        if b.fleet_sunk():
            return move


if __name__ == "__main__":

    print("what fleet should be used? (leave empty for default = [5, 4,4, 3,3,3, 2,2,2,2])")
    fleet_str = input()
    if fleet_str:
        fleet = list(map(int, fleet_str.strip('\n').split(',')))
    else:
        fleet = None

    # play_1p_game(fleet)
    print(f"random game for fleet took {simulate_random_strategy(fleet)} moves")
