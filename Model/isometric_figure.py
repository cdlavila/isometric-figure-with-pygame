import pygame
from Functions import translation_transformation as tt


class IsometricFigure:
    # Constructor
    def __init__(self, surface, size, color=[0, 0, 0]):
        self.__points = []
        self.__surface = surface
        self.__size = size
        self.__color = color

    # Getters and Setters
    @property
    def points(self):
        return self.__points

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def draw(self):
        center = [self.__surface.get_width() / 2, self.__surface.get_height() / 2]
        points = []
        # Create all points of around
        points.append([0, 0])
        points.append([0, self.__size])
        points.append([self.__size, self.__size + self.__size / 2])
        points.append([points[len(points) - 1][0], points[len(points) - 1][1] + self.__size])
        points.append([points[len(points) - 1][0] + self.__size, points[len(points) - 1][1] + self.__size / 2])
        points.append([points[len(points) - 1][0] + self.__size * 2, points[len(points) - 2][1] - self.__size / 2])
        points.append([self.__size * 4, points[0][1]])
        points.append([self.__size * 3, (0 - self.__size) / 2])
        points.append([self.__size * 2, 0 - self.__size])
        points.append(points[0])
        # Create all rest of points
        points.append([self.__size * 3, points[5][1] - self.__size / 2])
        points.append([self.__size * 2, self.__size])
        points.append([points[2][0], self.__size - self.__size / 2])

        # Translate all points to cartesian plane
        translatedPoints = []
        for point in points:
            translatedPoints.append(tt.translationTransformation(center, point))

        # Draw all points
        for point in translatedPoints:
            pygame.draw.circle(self.__surface, self.__color, point, 1)

        # Connect all points around with lines
        pointsAround = len(translatedPoints) - 4
        contador = 0
        while contador < pointsAround:
            initialPoint = translatedPoints[contador]
            endPoint = translatedPoints[contador + 1]
            pygame.draw.line(self.__surface, self.__color, initialPoint, endPoint)
            contador += 1

        # Connect the rest of points with lines
        pygame.draw.line(self.__surface, self.__color, translatedPoints[3], translatedPoints[10])
        pygame.draw.line(self.__surface, self.__color, translatedPoints[10], translatedPoints[7])
        pygame.draw.line(self.__surface, self.__color, translatedPoints[2], translatedPoints[11])
        pygame.draw.line(self.__surface, self.__color, translatedPoints[11], translatedPoints[7])
        pygame.draw.line(self.__surface, self.__color, translatedPoints[11], translatedPoints[12])
        pygame.draw.line(self.__surface, self.__color, translatedPoints[12], translatedPoints[8])
        pygame.draw.line(self.__surface, self.__color, translatedPoints[12], translatedPoints[1])

        self.__points = translatedPoints
