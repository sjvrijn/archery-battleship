"""Play a game of Battleship"""

from itertools import count, product
from random import shuffle
from typing import Sequence

from battleship.board import Board
from battleship.ship import ShipPartState, NONE_SHIP


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
    for move, (r,c) in enumerate(shots, start=1):
        b.shoot(r,c)
        if b.fleet_sunk():
            return move

def simulate_random_with_search_strategy(fleet: Sequence[int]) -> int:
    """Simulate a strategy of shooting randomly, but searching logically on a hit to sink a ship"""
    b = Board()
    b.place_random_fleet(fleet)

    shots = list(product(range(b.size), range(b.size)))
    shuffle(shots)

    state = 'exploring'

    for move in count(1):

        if state == 'exploring':
            next_shot = shots.pop()
            result = b.shoot(*next_shot)
            if result == ShipPartState.HIT:
                state = 'exploiting'
                ship_core = next_shot
                next_direction = (1,0)

        elif state == 'exploiting':
            next_shot, next_direction = select_next_valid_shot_and_direction(b, ship_core, next_direction)
            shots.remove(next_shot)
            result = b.shoot(*next_shot)
            if result == ShipPartState.HIT:
                next_direction = step_direction(next_direction)
            elif result == ShipPartState.MISS:
                next_direction = select_next_direction(next_direction)
            elif result == ShipPartState.SUNK:
                state = 'exploring'

        if b.fleet_sunk():
            return move

def simulate_filtered_random_with_search_strategy(fleet: Sequence[int]) -> int:
    """Simulate a strategy of shooting randomly, but searching logically on a hit to sink a ship"""
    b = Board()
    b.place_random_fleet(fleet)

    shots = [(r,c) for r,c in product(range(b.size), range(b.size)) if (r+c)%2 == 1]
    shuffle(shots)

    state = 'exploring'

    for move in count(1):

        if state == 'exploring':
            next_shot = shots.pop()
            result = b.shoot(*next_shot)
            if result == ShipPartState.HIT:
                state = 'exploiting'
                ship_core = next_shot
                next_direction = (1,0)

        elif state == 'exploiting':
            next_shot, next_direction = select_next_valid_shot_and_direction(b, ship_core, next_direction)
            try:
                shots.remove(next_shot)  # remove 'searching-shot' if in list of shots to try
            except ValueError:
                pass
            result = b.shoot(*next_shot)
            if result == ShipPartState.HIT:
                next_direction = step_direction(next_direction)
            elif result == ShipPartState.MISS:
                next_direction = select_next_direction(next_direction)
            elif result == ShipPartState.SUNK:
                state = 'exploring'

        if b.fleet_sunk():
            return move

def select_next_valid_shot_and_direction(b, ship_core, next_direction):
    """For the current search, select the next valid shot.

    By default this would be the next one in the current search direction,
    but will turn to the next available direction if a previous MISS, HIT,
    or the edge of the board is reached.
    """
    next_shot = calc_next_shot(ship_core, next_direction)
    while not shot_is_valid(b, next_shot):
        next_direction = select_next_direction(next_direction)
        next_shot = calc_next_shot(ship_core, next_direction)
    return next_shot, next_direction

def calc_next_shot(ship_core, next_direction):
    """Determine 'next_shot' as ship_core offset with next_direction"""
    r, c = ship_core[0] + next_direction[0], ship_core[1] + next_direction[1]
    return (r, c)

def shot_is_valid(board, shot) -> bool:
    """Check if a proposed shot is valid to try?"""
    r, c = shot
    # Does proposed shot fall outside of the board?
    if r < 0 or r >= board.size or c < 0 or c >= board.size:
        return False
    # Has the target square not been shot at yet?
    target = board.field[r][c][0].parts[board.field[r][c][1]]
    if target not in [ShipPartState.NONE, ShipPartState.SAFE]:  # todo make black-box checkable?
        return False
    return True

def step_direction(next_direction):
    """Move 'next_direction' forward one step in its current direction"""
    dr, dc = next_direction
    if dr > 0:
        dr += 1
    elif dr < 0:
        dr -= 1
    elif dc > 0:
        dc += 1
    elif dc < 0:
        dc -= 1
    return dr, dc

def select_next_direction(direction: tuple[int]) -> tuple[int]:
    """Change direction in following order: (1,0) -> (0,1) -> (-1,0) -> (0,-1)"""
    dr, dc = direction
    if dr > 0:
        dr, dc = 0, 1
    elif dc > 0:
        dr, dc = -1, 0
    elif dr < 0:
        dr, dc = 0, -1
    else:
        raise ValueError("All directions tried")
    return dr, dc


if __name__ == "__main__":

    print("what fleet should be used? (leave empty for default = [5, 4,4, 3,3,3, 2,2,2,2])")
    fleet_str = input()
    if fleet_str:
        fleet = list(map(int, fleet_str.strip('\n').split(',')))
    else:
        fleet = None

    # play_1p_game(fleet)

    min_shots = sum(fleet) if fleet else sum([5, 4,4, 3,3,3, 2,2,2,2])
    print(f"\nA game with this fleet needs {min_shots} shots in a perfect game\n")

    strategies = {
        'random': simulate_random_strategy,
        'random with search': simulate_random_with_search_strategy,
        'filtered random with search': simulate_filtered_random_with_search_strategy,
    }

    for name, strategy in strategies.items():

        num_games = 10_000
        durations = []
        for _ in range(num_games):
            try:
                num_moves = strategy(fleet)
            except ValueError:
                num_games -= 1
                continue
            durations.append(num_moves)
        durations.sort()

        q1, q2, q3 = durations[num_games//4], durations[num_games//2], durations[3*(num_games//4)]
        avg = sum(durations) / num_games

        print(f"An average {name} game ({num_games} tries) takes {avg:.2f} moves.")
        print(f"    quantiles: [{min(durations)}, {q1}, {q2}, {q3}, {max(durations)}]")
