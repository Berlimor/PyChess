import pygame


class Tile():
    # X - rows, Y - cols
    def __init__(self, row: int, col: int, size: int, piece = None ) -> None:
        self.row = row
        self.col = col
        self.pos = (row, col)
        self.size = size
        self.rect = (
            col * size,
            row * size,
            size,
            size
        )

        self.piece = piece

        light, dark = (181, 136, 99), (240, 217, 181)
        self.color = light if (row + col) % 2 == 0 else dark
        self.highlighted = False
        self.highlighted_color = (171, 162, 58) if self.color == dark else (206, 210, 107)

    
    # Get an in game position notation
    def get_game_pos(self, pos: tuple) -> str:
        columns = 'abcdefgh'
        return columns[pos[1]] + str(pos[0])
    

    # Draw the tile on display
    def draw(self, display) -> None:
        if not self.highlighted:
            pygame.draw.rect(display, self.highlighted_color, self.rect)
        else:
            pygame.draw.rect(display, self.color, self.rect)


    # Draw the occupying piece inside the tile
    def draw_piece(self, piece) -> None:
        if self.piece != None:
            img_rect = piece.img.get_rect()
            img_rect.center = self.rect.center()