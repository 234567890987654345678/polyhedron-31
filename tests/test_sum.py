from pytest import approx
from math import *
from shadow.polyedr import Polyedr


class TestPolyedr:

    def test_1(self):
        assert Polyedr(f"data/test1.geom").sum_of_edges == 3

    def test_2(self):
        assert Polyedr(f"data/test2.geom").sum_of_edges == approx(2*sqrt(6))

    def test_3(self):
        assert Polyedr(f"data/test3.geom").sum_of_edges == 0
