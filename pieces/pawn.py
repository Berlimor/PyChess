import pygame

from .piece import Piece
from board.board import Board
from board.square import Square

class Pawn(Piece):
    def __init__(self, pos: tuple, color: str, board: Board) -> None:
        super().__init__(pos, color, board)
        self.name = 'P'
        img_path = '../assets/pieces-img/' + color[0] + self.name
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.width_cell - 35, board.height_cell - 35))

    def get_possible_moves(self, board: Board):
        possible_moves = []
        moves = []
        