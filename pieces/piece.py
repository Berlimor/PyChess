import pygame

from board.square import Square
from board.board import Board

class Piece:
    def __init__(self, pos, color) -> None:
        self.color = color
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.has_moved = False

    def get_moves(self, board: Board) -> list[Square]:
        moves = []
        for direction in self.get_possible_moves(board):
            for square in direction:
                if square.piece != None:
                    if square.piece.color != self.color:
                        moves.append(square)
                        break
                    else: 
                        break
                else:
                    moves.append(square)
    
        return moves
    
    def get_valid_moves(self, board: Board) -> list[Square]:
        valid_moves = []
        for square in self.get_moves(board):
            if not board.in_check(self.color, board_change=[self.pos, square.pos]):
                valid_moves.append(square)

        return valid_moves
    
    def move(self, board: Board, square: Square, force: bool = False) -> bool:
        for i in board.squares:
            i.highlight = False
        if square in self.get_valid_moves() or force:
            prev_square = board.get_piece_by_pos(self.pos)
            self.pos, self.x, self.y = square.pos, square.x, square.y
            prev_square.piece = None
            square.piece = self
            board.selected = None
            self.has_moved = True

            # Pawn promotion
            if self.name == 'P':
                if self.y == 0 or self.x == 7:
                    from pieces.queen import Queen
                    square.piece = Queen((self.x, self.y), self.color, board)

            # Move rook if king castles
            if self.name == 'K':
                if prev_square.x - self.x == 2:
                    rook = board.get_piece_by_pos((0, self.y))
                    rook.move(board, board.get_square_by_pos((5, self.y)), force=True)
                elif prev_square.x - self.x == -2:
                    rook = board.get_piece_by_pos((7, self.y))
                    rook.move(board, board.get_square_by_pos((5, self.y)), force=True)
            
            return True
        else: 
            board.selected = None
            return False
        
    def attack(self, board: Board) -> list[Square]:
        return self.get_moves(board=board)