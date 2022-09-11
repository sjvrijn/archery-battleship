"""Class for a board in a game of BattleShip"""

from .ship import Ship, ShipPartState, NONE_SHIP


state_print_parse = {
    ShipPartState.NONE: '.',
    ShipPartState.SAFE: 'O',
    ShipPartState.HIT: 'X',
}


class Board:

    def __init__(self, size: int=10):
        if size < 3:
            raise ValueError("The size of a board should be at least 3.")

        self.size = size
        self.field = [
            [(NONE_SHIP, 0) for _ in range(size)]
            for _ in range(size)
        ]

    def place_ship(self, size: int, x: int, y: int, horizontal: bool):
        """Place a ship of `size` at (x,y) on the board"""
        if not (0 <= x < self.size):
            raise ValueError(f"x={x} is invalid, must be 0..{self.size-1}")
        if not (0 <= y < self.size):
            raise ValueError(f"y={y} is invalid, must be 0..{self.size-1}")

        ship = Ship(size)
        for i in range(size):
            if horizontal:
                self.field[x][y+i] = (ship, i)
            else:
                self.field[x+i][y] = (ship, i)

    def __str__(self):
        """Display the whole board as a grid with ./O/X for empty/safe/hit"""
        return '\n'.join([
            ''.join(
                [
                    state_print_parse[ship.parts[i]]
                    for ship, i in row
                ]
            )
            for row in self.field
        ])
