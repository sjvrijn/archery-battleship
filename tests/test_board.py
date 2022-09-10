from battleship.board import Board


def test_str_empty_board():
    b = Board(4)
    assert str(b) == '....\n....\n....\n....'
