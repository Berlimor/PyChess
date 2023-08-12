import pygame

class Square():
    def __init__(self, x: int, y: int, width_cell: int, height_cell: int) -> None:
        self.x = x #Row
        self.y = y #Column
        self.pos = (x, y)

        self.width_cell = width_cell
        self.height_cell = height_cell

        self.board_x = x * width_cell
        self.board_y = y * height_cell
        self.board_pos = (self.board_x, self.board_y) #Where the square would be drawn in a window

        self.color = 'light' if x + y % 2 == 0 else 'dark'
        self.draw_color = (239, 197, 113) if self.color == 'light' else (215, 157, 41)
        self.draw_highlight_color = (226, 173, 68) if self.color == 'light' else (206, 144, 18)
        self.highlight = False
        
        self.piece = None
        self.position = self.get_position()
        self.rect = pygame.Rect(
            self.board_x, 
            self.board_y, 
            self.width_cell, 
            self.height_cell
        )


    #Get the fomlal name of the square
    def get_position(self):
        columns = 'abcdefgh'
        return (columns[self.x], self.y + 1)
    
    #Get the color of the square
    def draw(self, display):
        if self.highlight:
            pygame.draw.rect(display, self.draw_highlight_color, self.rect)
        else: 
            pygame.draw.rect(display, self.draw_color, self.rect)
        
        if self.piece != None:
            centering_rect = self.piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.piece.img, centering_rect.topleft)