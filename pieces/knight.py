from piece import Piece
from board.board import Board
from board.tile import Tile

class Knight(Piece):
    def __init__(self, pos: tuple, color: str) -> None:
        super().__init__(pos, color)
        self.name = 'N'

    def get_moves(self, board: Board):
        ...