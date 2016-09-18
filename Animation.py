from Shapes.Point import Point
import math

def rotate_around(center, point, angle):
    x = (point.x - center.x) * math.cos(angle) - (point.y - center.y) * math.sin(angle) + center.x
    y = (point.y - center.y) * math.cos(angle) + (point.x - center.x) * math.sin(angle) + center.y
    return Point(x, y)

def sampling(n):
    return 2.0 * math.pi / (n - 1)