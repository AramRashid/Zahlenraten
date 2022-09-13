import unittest
from website.game import calc_points, get_status

class GameTest(unittest.TestCase):
    def setUp(self):
        self.guesses = 5
        self.rnd_number = 72

    def test_get_points(self):
        self.assertEqual(calc_points(self.guesses), 50)

    def test_get_status(self):
        self.assertEqual(get_status(10, self.rnd_number), 'Höher')
        self.assertEqual(get_status(80, self.rnd_number), 'Tiefer')
        self.assertEqual(get_status(72, self.rnd_number), 'Gewonnen')