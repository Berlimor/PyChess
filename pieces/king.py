from piece import Piece
from board.board import Board
from board.tile import Tile

class King(Piece):
    def __init__(self, pos: tuple, color: str) -> None:
        super().__init__(pos, color)
        self.name = 'K'

    def get_moves(self, board: Board) -> list[Tile]:
        moves = []
        pos_moves = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]
        

        return moves