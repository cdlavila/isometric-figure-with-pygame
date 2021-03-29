import pygame
from Model import isometric_figure


if __name__ == '__main__':
    black = [0, 0, 0]
    lightBlue = [48, 187, 246]
    width = height = 600

    # Open screen
    pygame.init()
    screen = pygame.display.set_mode([width, height])

    # Creates isometric figure
    figure = isometric_figure.IsometricFigure(25, lightBlue)
    figure.draw(screen)

    # Keeps screen opended
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                screen.fill(black)
                if event.key == pygame.K_UP:
                    figure.scaling(0.1)
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    figure.scaling(-0.1)
                    pygame.display.flip()
                if event.key == pygame.K_RIGHT:
                    figure.rotate(1)
                if event.key == pygame.K_LEFT:
                    figure.rotate(-1)
        pygame.display.flip()
