"""Class for a board in a game of BattleShip"""

from enum import Enum


class ShipPartState:
    NONE = 0
    SAFE = 1
    HIT = 2


state_print_parse = {
    ShipPartState.NONE: '.',
    ShipPartState.SAFE: 'O',
    ShipPartState.HIT: 'X',
}


class Board:

    def __init__(self, size=10):
        self.size = size
        self.field = [
            [ShipPartState.NONE for _ in range(size)]
            for _ in range(size)
        ]

    def place_ship(self, size: int, x: int, y: int, horizontal: bool):
        """Place a ship of `size` at (x,y) on the board"""
        if not (0 <= x < self.size):
            raise ValueError(f"x={x} is invalid, must be 0..{self.size-1}")
        if not (0 <= y < self.size):
            raise ValueError(f"y={y} is invalid, must be 0..{self.size-1}")

        if horizontal:
            for i in range(y, y+size):
                self.field[x][i] = ShipPartState.SAFE
        else:
            for i in range(x, x+size):
                self.field[i][y] = ShipPartState.SAFE

    def __str__(self):
        """Display the whole board as a grid with ./O/X for empty/safe/hit"""
        return '\n'.join(
            ''.join(state_print_parse[square] for square in row)
            for row in self.field
        )
