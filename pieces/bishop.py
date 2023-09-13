from piece import Piece
from board.tile import Tile
from board.board import Board

class Bishop(Piece):
    def __init__(self, pos: tuple, color: str) -> None:
        super().__init__(pos, color)
        self.name = 'B'

    def get_moves(self, board: Board) -> list[Tile]:
        moves = []
        for i in range(4):
            match i:
                case 0:
                    row = self.row - 1
                    col = self.col - 1
                    while row > 0 & col > 0:
                        tile = board.get_tile_by_pos((row, col))
                        moves.append(tile)
                        if tile.piece != None:
                            row = 0
                        row -= 1
                        col -= 1
                case 1:
                    row = self.row - 1
                    col = self.col + 1
                    while row > 0 & col < 8:
                        tile = board.get_tile_by_pos((row, col))
                        moves.append(tile)
                        if tile.piece != None:
                            row = 0
                        row -= 1
                        col += 1
                case 2:
                    row = self.row + 1
                    col = self.col + 1
                    while row < 8 & col < 8:
                        tile = board.get_tile_by_pos((row, col))
                        moves.append(tile)
                        if tile.piece != None:
                            row = 8
                        row += 1
                        col += 1
                case 3:
                    row = self.row + 1
                    ool = self.col - 1
                    while row < 8 & col > 0:
                        tile = board.get_tile_by_pos((row, col))
                        moves.append(tile)
                        if tile.piece != None:
                            row = 8
                        row += 1
                        col -= 1
                case _:
                    print("Error in bishop get moves")
                    return
        
        return moves

