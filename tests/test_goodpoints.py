import unittest
from pytest import approx

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    def test1(self):
        self.polyedr = Polyedr("data/testfigure1.geom")
        self.assertEqual(self.polyedr.get_sum_of_good_edges(), 260)

    def test2(self):
        self.polyedr = Polyedr("data/testfigure2.geom")
        self.assertEqual(self.polyedr.get_sum_of_good_edges(), 260)

    def test3(self):
        self.polyedr = Polyedr("data/testfigure3.geom")
        self.assertEqual(self.polyedr.get_sum_of_good_edges(), approx(100))
