import unittest
from src.game import *

class TestGame(unittest.TestCase):

    def test_return_a_string(self):
        answer = return_a_string(7)
        self.assertEqual("7", answer)

    def test_fizz(self):
        self.assertEqual("Fizz", fizz_divisible_by_3(3))

    def test_buzz(self):
        self.assertEqual("Buzz", buzz_divisible_by_5(5))

    def test_fizz_buzz(self):
        self.assertEqual("Fizz Buzz", fizz_buzz_divisible_by_15(15))

    def test_fizzbuzz_game(self):
        game_range = 51
        fizzbuzz_game(game_range)
        self.assertEqual("Fizz", fizz_divisible_by_3(3))
        self.assertEqual("Buzz", buzz_divisible_by_5(5))
        self.assertEqual("Fizz Buzz", fizz_buzz_divisible_by_15(15))
