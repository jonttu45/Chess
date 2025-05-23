import pygame
from pygame.locals import *
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 1024, 1024

        self.board_rows = 8
        self.board_cols = 8
        self.square_size = self.width // self.board_cols

        # Colors (RGB)
        self.color_light = (238, 238, 210)
        self.color_dark = (118, 150, 86)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Chessboard")
        self._running = True
 
    #proceeds events like pressed keys, mouse motion etc.
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    #compute changes in the game world like NPC's moves, player moves, AI, game score.
    def on_loop(self):
        pass

    #handles graphics.
    def on_render(self):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                color = self.color_light if (row + col) % 2 == 0 else self.color_dark
                pygame.draw.rect(
                    self._display_surf,
                    color,
                    (col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                )
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()