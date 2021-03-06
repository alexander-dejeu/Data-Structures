#!python

from strings import is_palindrome
from strings import is_containing
import unittest


class StringsTest(unittest.TestCase):

    def test_string_search_no_matches(self):
        assert is_containing('alex', '3x3') is False
        assert is_containing('fourdogs', 'sgodruof') is False
        assert is_containing('1234', '12345') is False
        assert is_containing('', 'a') is False

    def test_string_search_matches(self):
        assert is_containing('', '') is True
        assert is_containing('helloworld', 'helloworld')
        assert is_containing('123', '12')
        assert is_containing('!23$5^&*', '$')

    def test_is_palindrome_with_mirrored_strings(self):
        # simple palindromes that are mirrored strings
        assert is_palindrome('') is True  # base case
        assert is_palindrome('A') is True  # base case
        assert is_palindrome('BB') is True
        assert is_palindrome('LOL') is True
        assert is_palindrome('noon') is True
        assert is_palindrome('radar') is True
        assert is_palindrome('racecar') is True

    def test_is_palindrome_with_mixed_casing(self):
        # palindromes with mixed leter casing
        assert is_palindrome('Bb') is True
        assert is_palindrome('NoOn') is True
        assert is_palindrome('Radar') is True
        assert is_palindrome('RaceCar') is True

    def test_is_palindrome_with_whitespace(self):
        # palindromes with whitespace
        assert is_palindrome('taco cat') is True
        assert is_palindrome('race car') is True
        assert is_palindrome('race fast safe car') is True

    def test_is_palindrome_with_whitespace_and_mixed_casing(self):
        # palindromes with whitespace and mixed letter casing
        assert is_palindrome('Taco Cat') is True
        assert is_palindrome('Race Car') is True
        assert is_palindrome('Race Fast Safe Car') is True

    def test_is_palindrome_with_whitespace_and_punctuation(self):
        # palindromes with whitespace and punctuation
        assert is_palindrome('taco cat!') is True
        assert is_palindrome('race, car!!') is True
        assert is_palindrome('race fast, safe car.') is True

    def test_is_palindrome_with_mixed_casing_and_punctuation(self):
        # palindromes with whitespace, punctuation and mixed letter casing
        assert is_palindrome('Race fast, safe car.') is True
        assert is_palindrome('Was it a car or a cat I saw?') is True
        assert is_palindrome("Go hang a salami, I'm a lasagna hog.") is True
        assert is_palindrome('A man, a plan, a canal - Panama!') is True

    def test_is_palindrome_with_non_palindromic_strings(self):
        assert is_palindrome('AB') is False
        assert is_palindrome('ABC') is False
        assert is_palindrome('doge') is False
        assert is_palindrome('monkey') is False
        assert is_palindrome('chicken, monkey!') is False


if __name__ == '__main__':
    unittest.main()
