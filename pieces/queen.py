from piece import Piece
from bishop import Bishop
from rook import Rook
from board.board import Board
from board.tile import Tile

class Queen(Piece):
    def __init__(self, pos: tuple, color: str) -> None:
        super().__init__(pos, color)
        self.name = 'Q'

    def get_moves(self, board: Board) -> list[Tile]:
        bishop_set = Bishop.get_moves(self, board)
        rook_set = Rook.get_moves(self, board)
        moves = bishop_set + rook_set
                
        return moves