import pygame

from piece import Piece
from board.board import Board
from board.tile import Tile

class Pawn(Piece):
    def __init__(self, pos: tuple, color: str, board: Board) -> None:
        super().__init__(pos, color, board)
        self.name = 'P'
        self.has_moved = False

    def get_moves(self, board: Board) -> list[Tile]:
        moves = []
        if self.color == 'w':
            if self.x - 1 >= 0:
                tile = board.get_tile_by_pos((self.x - 1, self.y))
                if tile.piece is None:
                    moves.append(tile)

            if not self.has_moved & self.x - 2 >= 0:
                tile = board.get_tile_by_pos((self.x - 2, self.y))
                if tile.piece is None:
                    moves.append(tile)

            # Check for an attack opportunity
            if board.get_tile_by_pos((self.x - 1, self.y - 1)).piece != None:
                moves.append(board.get_tile_by_pos((self.x - 1, self.y - 1)))
            if board.get_tile_by_pos((self.x - 1, self.y + 1)).piece != None:
                moves.append(board.get_tile_by_pos((self.x - 1, self.y + 1)))

        else: 
            if self.x + 1 <= 8:
                tile = board.get_tile_by_pos((self.x + 1, self.y))
                if tile.piece is None:
                    moves.append(tile)
            if not self.has_moved & self.x + 2 <= 8:
                tile = board.get_tile_by_pos((self.x + 2, self.y))
                if tile.piece is None:
                    moves.append(tile)
            
            if board.get_tile_by_pos((self.x + 1, self.y - 1)).piece != None:
                moves.append(board.get_tile_by_pos((self.x + 1, self.y - 1)))
            if board.get_tile_by_pos((self.x + 1, self.y + 1)).piece != None:
                moves.append(board.get_tile_by_pos((self.x + 1, self.y + 1)))
        

        return moves
    
    
    def move(self, dest_pos: tuple, board: Board) -> None:
        dest_tile = board.get_tile_by_pos(dest_pos)
        if dest_tile.piece != None:
            eaten_piece = dest_tile.piece
            board.eaten_pieces.append(eaten_piece)
        board.tiles[self.row][self.col] = Tile(self.row, self.col, board.cell_size)
        board.tiles[dest_pos[0]][dest_pos[1]] = Tile(dest_pos[0], dest_pos[1], board.cell_size, self)
        self.pos = dest_pos
        self.has_moved = True
        self.row, self.col = dest_pos
        dest_tile.piece = self

        # Check if the position allows this pawn to turn into the Queen
        ...