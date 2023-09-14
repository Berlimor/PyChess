from piece import Piece
from board.board import Board
from board.tile import Tile

class Rook(Piece):
    def __init__(self, pos: tuple, color: str) -> None:
        super().__init__(pos, color)
        self.name = 'R'

    def get_moves(self, board: Board) -> list[Tile]:
        moves = []
        for i in range(4):
            match i:
                case 0:
                    row = self.row - 1
                    while row >= 0:
                        tile = board.get_tile_by_pos((row, self.col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                            row = -1
                        else: 
                            moves.append(tile)
                        row -= 1
                case 1:
                    col = self.col + 1
                    while col < 8:
                        tile = board.get_tile_by_pos((row, self.col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                            col = 8
                        else: 
                            moves.append(tile)
                        col += 1
                case 2:
                    row = self.row + 1
                    while row < 8:
                        tile = board.get_tile_by_pos((row, self.col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                            row = 8
                        else: 
                            moves.append(tile)
                        row += 1
                case 3:
                    col = self.col - 1
                    while col >= 0:
                        tile = board.get_tile_by_pos((row, self.col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                            col -= 1
                        else: 
                            moves.append(tile)
                        col -= 1
                case _:
                    print("Error in rook get moves")
                    return
                
        return moves