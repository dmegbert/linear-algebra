from math import sqrt, acos, degrees
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        return Vector([Decimal(scalar) * x for x in self.coordinates])

    def magnitude(self):
        """Returns a float of the magnitude (distance) of the vector"""
        return Decimal(sqrt(sum([x ** Decimal(2) for x in self.coordinates])))

    def normalized(self):
        """Returns a normal vector (magnitude of 1) in the direction of the given vector"""
        try:
            return self.scalar_multiply(Decimal('1.0') / self.magnitude())

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot_product(self, vector):
        if self.dimension != vector.dimension:
            raise ValueError('The vectors must have the same dimension')

        return sum(self.coordinates[i] * vector.coordinates[i] for i in range(vector.dimension))

    def angle(self, vector, in_degrees=False):
        """
        Compute the measure of an angle between two vectors
        :param vector
        :returns Float of angle measure in radians
        """
        try:
            u1 = self.normalized()
            u2 = vector.normalized()
            if in_degrees:
                return degrees(acos(u1.dot_product(u2)))
            return acos(u1.dot_product(u2))
        except Exception as exp:
            if str(exp) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with zero vector')
            else:
                raise exp

# a = Vector([1,1])
# b = Vector([1, 0])
