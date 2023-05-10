from pytest import approx
from math import *
from shadow.polyedr import Polyedr


class TestPolyedr:

    def test_1(self):
        assert Polyedr(f"data/test1.geom").sum_of_edges == 3

    def test_2(self):
        assert Polyedr(f"data/test2.geom").sum_of_edges == approx(2 * sqrt(6))

    def test_3(self):
        assert Polyedr(f"data/test3.geom").sum_of_edges == 0

    def test_4(self):
        assert Polyedr(f"data/test4.geom").sum_of_edges == approx((5 + sqrt(61)) * (1 / 2))

    def test_5(self):
        assert Polyedr(f"data/test5.geom").sum_of_edges == approx(sqrt(26) + sqrt(17))

    def test_6(self):
        assert Polyedr(f"data/test6.geom").sum_of_edges == approx(sqrt(17) / 2 + 2)
