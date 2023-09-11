import pygame

from board.board import Board

class Piece:
    def __init__(self, pos: tuple, color: str) -> None:
        self.color = color
        self.pos = pos
        self.row = pos[0]
        self.col = pos[1]
        self.selected = False


    def get_valid_moves(self, board):
        moves = self.get_moves(board)