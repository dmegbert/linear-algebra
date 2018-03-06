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
