import pygame
from Model import isometric_figure


if __name__ == '__main__':
    lightBlue = [48, 187, 246]
    width = height = 600

    # Open screen
    pygame.init()
    screen = pygame.display.set_mode([width, height])

    # Creates isometric figure
    figure = isometric_figure.IsometricFigure(screen, 30, lightBlue)
    figure.draw()

    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        pygame.display.flip()
