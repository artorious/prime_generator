import unittest
from prime_generator import primeNumbers

class TestPrimeNumbers(unittest.TestCase):
    
    def test_for_accurate_results(self):
        """test that list only contains primes."""
        self.assertEqual(primeNumbers(9), [1, 2, 3, 5, 7])
    #
    def test_input_is_integer(self):
        """test that argument from user is an interger"""
        with self.assertRaises(TypeError):
            primeNumbers([])

    def test_input_is_not_negative(self):
        """ test that argument from user is not negative"""
        with self.assertRaises(TypeError):
            primeNumbers(-1)

    def test_inclusivity_of_n(self):
        """test that n is included in results if it is prime"""
        self.assertNotEqual(primeNumbers(7), [1, 2, 3, 5])

    def test_one_is_prime(self):
        """test that one is included as a prime."""
        self.assertIn(1, primeNumbers(3))

if __name__ == '__main__':
    unittest.main()
