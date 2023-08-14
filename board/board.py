import pygame

from square import Square
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook

class Board:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.width_cell = width // 8
        self.height_cell = height // 8
        
        self.selected = None #The piece user clicked
        self.turn = 'w'
        self.board_model = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP']
            ['','','','','','','','']
            ['','','','','','','','']
            ['','','','','','','','']
            ['','','','','','','','']
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.squares = self.draw_squares()

    def draw_squares(self) -> list[list[Square]]:
        output = []
        for row in range(8):
            for col in range(8):
                output.append(Square(col, row, self.width_cell, self.height_cell))
        return output

    def get_square_by_pos(self, pos: tuple) -> Square:
        for square in self.squares:
            if square.pos == pos:
                return square

    def get_piece_by_pos(self, pos: tuple):
        return self.get_square_by_pos(pos).piece
    

    def create_board(self) -> None:
        for y, row in enumerate(self.board_model):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square_by_pos((x, y))
                    color = 'white' if piece[0] == 'w' else 'black'
                    match piece[1]:
                        case 'B':
                            square.piece = Bishop((x,y), color)
                        case 'K':
                            square.piece = King((x,y), color)
                        case 'N':
                            square.piece = Knight((x,y), color)
                        case 'P':
                            square.piece = Pawn((x,y), color)
                        case 'Q':
                            square.piece = Queen((x,y), color)
                        case 'R':
                            square.piece = Rook((x,y), color)
                        case _:
                            print("An error occured!")


    def handle_click(self, x_click, y_click) -> None:
        x = x_click // self.width_cell
        y = y_click // self.height_cell
        clicked_square = self.get_square_by_pos((x,y))

        if self.selected == None and clicked_square != None and clicked_square.piece.color == self.turn:
            self.selected = clicked_square.piece

        elif self.selected.move(self, clicked_square): #Move the piece to an empty square
            self.turn = 'w' if self.turn == 'b' else 'b'

        else: #Move the piece to a square with another piece
            if clicked_square.piece.color == self.turn:
                self.selected = clicked_square.piece

    def in_check(self, color: str, board_change=None) -> bool:
        is_in_check = False
        king_pos = None
        moving_piece = None
        old_square = None
        new_square = None
        new_square_old_piece = None

        if board_change != None:
            for square in self.squares:
                if square.pos == board_change[0]:
                    moving_piece = square.piece
                    old_square = square
                    old_square.piece = None

            for square in self.squares:
                if square.pos == board_change[1]:
                    new_square = square
                    new_square_old_piece = new_square.piece
                    new_square.piece = moving_piece

        pieces = [i.piece for i in self.squares if i.piece != None]

        if moving_piece != None:
            if moving_piece.name == 'K':
                king_pos = new_square.pos

            if king_pos == None:
                for piece in pieces:
                    if piece.name == 'K' and piece.color == color:
                        king_pos = piece.pos
            
            for piece in pieces:
                if piece.color != color:
                    for square in piece.attack_squares(self):
                        if square.pos == king_pos:
                            is_in_check = True

            if board_change != None:
                old_square.piece = moving_piece
                new_square.piece = new_square_old_piece

        return is_in_check
    
    def checkmate(self, color):
        is_in_checkmate = False
        pieces = [i.piece for i in self.squares if i.piece != None]

        for piece in pieces:
            if piece.name == 'K' and piece.color == color:
                king = piece

        if king.get_valid_moves(self) == None:
            if self.in_check(color=color):
                is_in_checkmate = True

        return is_in_checkmate
    
    def draw(self, display):
        if self.selected != None:
            self.get_square_by_pos(self.selected.pos).highlight = True
            for square in self.selected.get_valid_moves(self):
                square.highlight = True
        
        for square in self.squares:
            square.draw(display)