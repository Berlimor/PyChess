import pygame

from tile import Tile
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook

class Board:
    def __init__(self, size: int) -> None:
        # Width & height of the whole board, they must be equal and be divided by 8
        self.size = size

        # Width & Height of one tile
        self.cell_size = size // 8
        
        # The piece user clicked
        self.selected = None 
        self.turn = 'w'

        self.eaten_pieces = []

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
        
        self.tiles = self.draw_tiles()

    def draw_tiles(self) -> list[list[Tile]]:
        tile_grid = [[]]
        for row in range (8):
            for col in range(8):
                if self.board_model[row][col] != '':
                    match self.board_model[row][col][1]:
                        case 'B':
                            piece = Bishop((row, col), self.board_model[row][col][0], board=self)
                        case 'K':
                            piece = King((row, col), self.board_model[row][col][0], board=self)
                        case 'N':
                            piece = Knight((row, col), self.board_model[row][col][0], board=self)
                        case 'P':
                            piece = Pawn((row, col), self.board_model[row][col][0], board=self)
                        case 'Q':
                            piece = Queen((row, col), self.board_model[row][col][0], board=self)
                        case 'R':
                            piece = Rook((row, col), self.board_model[row][col][0], board=self)
                        case _:
                            print("Error!")
                
                tile = Tile(row, col, self.cell_size, piece)
                tile_grid[row].append(tile)

    
    def get_tile_by_pos(self, pos: tuple) -> Tile:
        row, col = pos
        return self.tiles[row][col]

    def select_by_click(self) -> None:
        click_pos = pygame.mouse.get_pos()
        ...

    def is_in_check(self) -> bool:
        ...

    def is_in_checkmate(self) -> bool:
        ...