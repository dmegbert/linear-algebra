from math import sqrt, acos, degrees
from functools import reduce

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, vector):
        if self.dimension != vector.dimension:
            raise ValueError('The vectors must have the same dimension')

        vector_sum_list = []
        for i in range(vector.dimension):
            vector_sum_list.append(self.coordinates[i] + vector.coordinates[i])

        return Vector(vector_sum_list)

    def subtract(self, vector):
        if self.dimension != vector.dimension:
            raise ValueError('The vectors must have the same dimension')

        return Vector([self.coordinates[i] - vector.coordinates[i] for i in range(vector.dimension)])

    def scalar_multiply(self, scalar):
        return Vector([scalar * x for x in self.coordinates])

    def magnitude(self):
        """Returns a float of the magnitude (distance) of the vector"""
        return sqrt(sum([x ** 2 for x in self.coordinates]))

    def normalized(self):
        """Returns a normal vector (magnitude of 1) in the direction of the given vector"""
        try:
            return self.scalar_multiply(1.0/ self.magnitude())

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def dot_product(self, vector):
        if self.dimension != vector.dimension:
            raise ValueError('The vectors must have the same dimension')

        return sum(self.coordinates[i] * vector.coordinates[i] for i in range(vector.dimension))

    def angle(self, vector):
        """
        Compute the measure of an angle between two vectors
        :param vector
        :returns Float of angle measure in radians
        """
        return acos(self.dot_product(vector) / (self.magnitude() * vector.magnitude()))
