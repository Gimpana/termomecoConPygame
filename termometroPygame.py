import pygame, sys
from pygame.locals import *

class mianApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termometro")
        self.__screen.fill((244,236,203))

    def __on_closed(self):
        pygame.quit()
        sys.exit()


    def star(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_closed()


            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    app = mianApp()
    app.star()