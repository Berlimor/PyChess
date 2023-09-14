from piece import Piece
from board.board import Board
from board.tile import Tile

class Knight(Piece):
    def __init__(self, pos: tuple, color: str) -> None:
        super().__init__(pos, color)
        self.name = 'N'

    def get_moves(self, board: Board) -> list[Tile]:
        moves = []
        for i in range(4):
            match i:
                case 0:
                    row = self.row - 2
                    col = self.col - 1
                    if row >= 0 & col >= 0:
                        tile = board.get_tile_by_pos((row, col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                        else:
                            moves.append(tile) 

                    row = self.row - 1
                    col = self.col - 2
                    if row >= 0 & col >= 0:
                        tile = board.get_tile_by_pos((row, col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                        else:
                            moves.append(tile) 
                case 1:
                    row = self.row - 2
                    col = self.col + 1
                    if row >= 0 & col < 8:
                        tile = board.get_tile_by_pos((row, col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                        else:
                            moves.append(tile) 

                    row = self.row - 1
                    col = self.col + 2
                    if row >= 0 & col < 8:
                        tile = board.get_tile_by_pos((row, col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                        else:
                            moves.append(tile) 
                case 2:
                    row = self.row + 2
                    col = self.col + 1
                    if row < 8 & col < 8:
                        tile = board.get_tile_by_pos((row, col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                        else:
                            moves.append(tile) 
                    
                    row = self.row + 1
                    col = self.col + 2
                    if row < 8 & col < 8:
                        tile = board.get_tile_by_pos((row, col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                        else:
                            moves.append(tile) 
                case 3:
                    row = self.row + 2
                    col = self.col - 1
                    if row < 8 & col >= 0:
                        tile = board.get_tile_by_pos((row, col))
                        if tile.piece != None:
                            if tile.piece.color != self.color:
                                moves.append(tile)
                        else:
                            moves.append(tile)    

                    row = self.row + 1
                    col = self.col - 2
                    if row < 8 & col >= 0:
                        tile = board.get_tile_by_pos((row, col))
                        moves.append(tile)
                case _:
                    print("Error in knight get moves")
                    return
                
        return moves
