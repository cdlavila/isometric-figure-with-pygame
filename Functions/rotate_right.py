import math


def rotateRight(point, degrees):
    x = point[0]
    y = point[1]
    xr = x * math.cos(math.radians(degrees)) + y * math.sin(math.radians(degrees))
    yr = -x * math.sin(math.radians(degrees)) + y * math.cos(math.radians(degrees))
    return [xr, yr]