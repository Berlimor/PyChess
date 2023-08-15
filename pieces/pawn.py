import pygame

from .piece import Piece
from board.board import Board
from board.square import Square

class Pawn(Piece):
    def __init__(self, pos: tuple, color: str, board: Board) -> None:
        super().__init__(pos, color, board)
        self.name = 'P'
        img_path = '../assets/pieces-img/' + color + self.name
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (60, 60))

    def get_possible_moves(self, board: Board) -> list[Square]:
        possible_moves = []
        moves = []
        if self.color == 'w':
            moves.append((0, -1))
            if not self.has_moved:
                moves.append((0, -2))
        else:
            moves.append((0, 1))
            if not self.has_moved:
                moves.append((0, 2))

        for move in moves:
            new_pos = (self.x, self.y + move[1])
            if new_pos[1] < 8 and new_pos[1] >= 0:
                possible_moves.append(new_pos)

        return possible_moves

    def get_moves(self, board: Board):
        moves = []
        for square in self.get_possible_moves(board=board):
            if square.occupying_piece != None:
                break
            else:
                moves.append(square)
        if self.color == 'w':
            if self.x + 1 < 8 and self.y - 1 >= 0:
                square = board.get_square_from_pos(
                    (self.x + 1, self.y - 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        moves.append(square)
            if self.x - 1 >= 0 and self.y - 1 >= 0:
                square = board.get_square_from_pos(
                    (self.x - 1, self.y - 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        moves.append(square)
        elif self.color == 'b':
            if self.x + 1 < 8 and self.y + 1 < 8:
                square = board.get_square_from_pos(
                    (self.x + 1, self.y + 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        moves.append(square)
            if self.x - 1 >= 0 and self.y + 1 < 8:
                square = board.get_square_from_pos(
                    (self.x - 1, self.y + 1)
                )
                if square.occupying_piece != None:
                    if square.occupying_piece.color != self.color:
                        moves.append(square)
        return moves

    def attacking_squares(self, board):
        moves = self.get_moves(board)
        # return the diagonal moves 
        return [i for i in moves if i.x != self.x]