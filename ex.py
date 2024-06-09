import numpy as np

def get_points(radius, number_of_points):
    radians_between_each_points = 2*np.pi/number_of_points
    list_of_points = []
    for p in range(0, number_of_points):
        list_of_points.append( (radius*np.cos(p*radians_between_each_points), radius*np.sin(p*radians_between_each_points)) )

    return list_of_points