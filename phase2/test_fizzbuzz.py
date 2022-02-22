import unittest

from fizzbuzz import fizzbuzz,generate

class TestFizzbuzz(unittest.TestCase):
  def test_lists_values_up_to_one(self):
    self.assertEqual(generate(1), "1")

  def test_fizz(self):
    for i in [3, 6, 9, 18]:
      print('testing', i)
      assert fizzbuzz(i) == 'Fizz'
  
  def test_buzz(self):
    for i in [5, 10, 20]:
      print('testing', i)
      assert fizzbuzz(i) == 'Buzz'

  def test_fizzbuzz(self):
    for i in [15, 30, 75]:
      print('testing', i)
      assert fizzbuzz(i) == 'FizzBuzz'