import pygame

from board.board import Board
from board.tile import Tile

class Piece:
    def __init__(self, pos: tuple, color: str) -> None:
        self.color = color
        self.pos = pos
        self.row = pos[0]
        self.col = pos[1]
        self.selected = False


    def move(self, dest_pos: tuple, board: Board, moves: list[Tile]) -> None:
        dest_tile = board.get_tile_by_pos(dest_pos)
        if dest_tile not in moves:
            return
        if dest_tile.piece != None:
            eaten_piece = dest_tile.piece
            board.eaten_pieces.append(eaten_piece)
        board.tiles[self.row][self.col] = Tile(self.row, self.col, board.cell_size)
        board.tiles[dest_pos[0]][dest_pos[1]] = Tile(dest_pos[0], dest_pos[1], board.cell_size, self)
        self.pos = dest_pos
        self.row, self.col = dest_pos
        dest_tile.piece = self