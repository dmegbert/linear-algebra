from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    THREE_PLACES = Decimal(10) ** -3

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

        return Decimal(sum(self.coordinates[i] * vector.coordinates[i] for i in range(vector.dimension)))

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
                return Decimal(degrees(acos(u1.dot_product(u2).quantize(self.THREE_PLACES))))
            return Decimal(acos(u1.dot_product(u2).quantize(self.THREE_PLACES)))
        except Exception as exp:
            if str(exp) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with zero vector')
            else:
                raise exp

    def round_to_three(self):
        return Vector([x.quantize(self.THREE_PLACES) for x in self.coordinates])

    def is_parallel(self, vector):
        if self.magnitude() == Decimal(0.0) or vector.magnitude() == Decimal(0.0):
            return True
        unit_vector_1 = self.normalized().round_to_three()
        unit_vector_2 = vector.normalized().round_to_three()
        opposite_unit_vector_2 = Vector([x * -1 for x in unit_vector_2.coordinates])
        return unit_vector_1 == unit_vector_2 or unit_vector_1 == opposite_unit_vector_2

    def is_orthogonal(self, vector):
        if self.magnitude() == Decimal(0.0) or vector.magnitude() == Decimal(0.0):
            return True
        return self.angle(vector, True) == Decimal(90)

    def vector_projection(self, vector):
        unit_vector = vector.normalized()
        my_scalar = self.dot_product(unit_vector)
        return unit_vector.scalar_multiply(my_scalar)

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def cross_product(self, vector):
        if self.dimension != 3 or vector.dimension != 3:
            raise ValueError('The vectors must both be 3 dimensional, dummy')
        if self.is_zero() or vector.is_zero() or self.angle(vector) == Decimal(0) or self.angle(vector) == pi:
            return Vector([0, 0, 0])
        x, y, z = self.coordinates
        a, b, c = vector.coordinates
        return Vector([(y * c - b * z), -(x * c - a * z), (x * b - a * y)])

