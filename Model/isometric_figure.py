import pygame
from Functions import translation_transformation as tt
from Functions import scaling as sc
from Functions import rotate_left as rl
from Functions import rotate_right as rr


class IsometricFigure:
    # Constructor
    def __init__(self, size, color=[255, 255, 255]):
        self.__surface = None
        self.__points = []
        self.__scaling = 1
        self.__rotation = 0
        self.__size = size
        self.__color = color

    # Getters and Setters
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

    def draw(self, surface):
        center = [surface.get_width() / 2, surface.get_height() / 2]
        size = self.__size

        if len(self.__points) == 0:
            points = []
            # Create all points of around
            points.append([0, 0])
            points.append([0, size])
            points.append([size, size + size / 2])
            points.append([points[len(points) - 1][0], points[len(points) - 1][1] + size])
            points.append([points[len(points) - 1][0] + size, points[len(points) - 1][1] + size / 2])
            points.append([points[len(points) - 1][0] + size * 2, points[len(points) - 2][1] - size / 2])
            points.append([size * 4, points[0][1]])
            points.append([size * 3, (0 - size) / 2])
            points.append([size * 2, 0 - size])
            points.append(points[0])
            # Create all rest of points
            points.append([size * 3, points[5][1] - size / 2])
            points.append([size * 2, size])
            points.append([points[2][0], size - size / 2])

            # Translate all points to cartesian plane
            translatedPoints = []
            for point in points:
                translatedPoints.append(tt.translationTransformation(center, point))
            print("\nIsometric figure has been drawn successfully")
            print(f"Simetric scaling: {self.__scaling}")
            print(f"Rotation: {self.__rotation}\n")
            self.__points = points
        else:
            translatedPoints = []
            for point in self.__points:
                translatedPoints.append(tt.translationTransformation(center, point))

        # Connect all points around with lines
        pointsAround = len(translatedPoints) - 4
        contador = 0
        while contador < pointsAround:
            initialPoint = translatedPoints[contador]
            endPoint = translatedPoints[contador + 1]
            pygame.draw.line(surface, self.__color, initialPoint, endPoint)
            contador += 1

        # Connect the rest of points with lines
        pygame.draw.line(surface, self.__color, translatedPoints[3], translatedPoints[10])
        pygame.draw.line(surface, self.__color, translatedPoints[10], translatedPoints[7])
        pygame.draw.line(surface, self.__color, translatedPoints[10], translatedPoints[5])
        pygame.draw.line(surface, self.__color, translatedPoints[2], translatedPoints[11])
        pygame.draw.line(surface, self.__color, translatedPoints[11], translatedPoints[7])
        pygame.draw.line(surface, self.__color, translatedPoints[11], translatedPoints[12])
        pygame.draw.line(surface, self.__color, translatedPoints[12], translatedPoints[8])
        pygame.draw.line(surface, self.__color, translatedPoints[12], translatedPoints[1])

        self.__surface = surface

    def scaling(self, n):
        if len(self.__points) > 0:
            if 0.3 <= round(self.__scaling + n, 1) <= 2:
                scaledPoints = []
                for point in self.__points:
                    scaledPoints.append(sc.scaling(point, [1 + n, 1 + n]))
                self.__scaling = round(self.__scaling + n, 1)
                self.__points = scaledPoints
                self.draw(self.__surface)
                print("Simetric scaling: ", self.__scaling)
            else:
                self.draw(self.__surface)

    def rotate(self, t):
        if len(self.__points) > 0:
            if -30 <= self.__rotation + t <= 30:
                rotatedPoints = []
                if t == 1:
                    for point in self.__points:
                        rotatedPoints.append(rr.rotateRight(point, t))
                if t == -1:
                    for point in self.__points:
                        rotatedPoints.append(rl.rotateLeft(point, t * (-1)))
                self.__rotation += t
                self.__points = rotatedPoints
                self.draw(self.__surface)
                if self.__rotation == 0:
                    print("Rotation: 0°")
                if self.__rotation > 0:
                    print(f"Hourly rotation: {self.__rotation}°")
                if self.__rotation < 0:
                    print(f"Anti-hourly rotation: {self.__rotation * (-1)}°")
            else:
                self.draw(self.__surface)
