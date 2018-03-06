import unittest
from hamcrest import assert_that, raises, calling, equal_to, contains
from algebra.vector import Vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.vec_2d = Vector([2, 3])
        self.vec_3d = Vector([1, 2, 3])
        self.vec_2d_negative = Vector([-4, -6])
        self.vec_3d_negative = Vector([-4, -6, -8])

    def test_add_when_diff_dimensions_raises_exception(self):
        assert_that(calling(self.vec_2d.add).with_args(self.vec_3d), raises(ValueError))

    def test_add_correct(self):
        sum_vec_2d = self.vec_2d.add(self.vec_2d_negative)
        sum_vec_3d = self.vec_3d.add(self.vec_3d_negative)

        assert_that(sum_vec_2d.coordinates[0], equal_to(-2))
        assert_that(sum_vec_2d.coordinates[1], equal_to(-3))

        assert_that(sum_vec_3d.coordinates[0], equal_to(-3))
        assert_that(sum_vec_3d.coordinates[1], equal_to(-4))
        assert_that(sum_vec_3d.coordinates[2], equal_to(-5))

    def test_subtract_diff_dimensions_raises_exception(self):
        assert_that(calling(self.vec_2d.subtract).with_args(self.vec_3d), raises(ValueError))

    def test_subtract_correct(self):
        diff_vec_2d = self.vec_2d.subtract(self.vec_2d_negative)
        diff_vec_3d = self.vec_3d.subtract(self.vec_3d_negative)

        assert_that(diff_vec_2d.coordinates, contains(6, 9))
        assert_that(diff_vec_3d.coordinates, contains(5, 8, 11))

    def test_scalar_multiply(self):
        assert_that(self.vec_2d.scalar_multiply(2).coordinates, contains(4, 6))
        assert_that(self.vec_3d.scalar_multiply(3).coordinates, contains(3, 6, 9))

    def test_equality(self):
        eq_vec = Vector([2, 3])
        assert_that(self.vec_2d.__eq__(eq_vec), True)
