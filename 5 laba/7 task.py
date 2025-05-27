def point_in_circle(x, y, radius):
    return x ** 2 + y ** 2 <= radius ** 2
print(point_in_circle(2, 3, 4))