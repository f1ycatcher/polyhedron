import unittest
from unittest.mock import patch, mock_open
from pytest import approx

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    def test1(self):
        fake_file_content = """100.0 0.0 0.0 0.0
4	2	6
0.8 0.6 1.0
0.0 0.0 0.0
2.4 1.0 1.0
1	2	4
3	1	2	3
3	4	3	2
"""
        fake_file_path = "data/holey_box.geom"
        with patch(
            "shadow.polyedr.open".format(__name__),
            new=mock_open(read_data=fake_file_content),
        ) as _file:
            self.polyedr = Polyedr(fake_file_path)
            self.assertEqual(self.polyedr.get_sum_of_good_edges(), approx(5.2))

    def test2(self):
        fake_file_content = """100 70 0 -135
4	2	6
0.8 0.6 1.0
0.0 0.0 0.0
2.4 1.0 1.0
1	2	4
3	1	2	3
3	4	3	2
"""
        fake_file_path = "data/holey_box.geom"
        with patch(
            "shadow.polyedr.open".format(__name__),
            new=mock_open(read_data=fake_file_content),
        ) as _file:
            self.polyedr = Polyedr(fake_file_path)
            self.assertEqual(self.polyedr.get_sum_of_good_edges(), approx(5.2))

    def test4(self):
        fake_file_content = """100.0 70 180 55
4	2	6
0.8 0.6 1.0
0.0 0.0 0.0
2.4 1.0 1.0
1	2	4
3	1	2	3
3	4	3	2
"""
        fake_file_path = "data/holey_box.geom"
        with patch(
            "shadow.polyedr.open".format(__name__),
            new=mock_open(read_data=fake_file_content),
        ) as _file:
            self.polyedr = Polyedr(fake_file_path)
            self.assertEqual(self.polyedr.get_sum_of_good_edges(), approx(5.2))

    def test3(self):
        fake_file_content = """100.0 0 100 0
4	2	6
0.8 0.6 1.0
0.0 0.0 0.0
2.4 1.0 1.0
1	2	4
3	1	2	3
3	4	3	2
"""
        fake_file_path = "data/holey_box.geom"
        with patch(
            "shadow.polyedr.open".format(__name__),
            new=mock_open(read_data=fake_file_content),
        ) as _file:
            self.polyedr = Polyedr(fake_file_path)
            self.assertEqual(self.polyedr.get_sum_of_good_edges(), approx(5.2))
