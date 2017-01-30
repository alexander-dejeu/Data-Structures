#!python

import string
import math
import re


def is_containing(text, substring):
    assert isinstance(text, str)
    assert isinstance(substring, str)
    return is_containing_iterative(text, substring)


def is_containing_iterative(text, substring):
    search_text_length = len(text)
    target_length = len(substring)

    if target_length > search_text_length:
        return False

    for i in range(0, search_text_length):
        window = text[i:i+target_length]
        if window == substring:
            return True
    if search_text_length == 0 and target_length == 0:
        return True
    return False


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    text = text.lower()
    text = re.sub("[^a-zA-Z]+", "", text)
    length = len(text)
    max_iterations = length/2

    for i in range(0, max_iterations):
        first_char = text[i]
        second_char = text[length - 1 - i]
        if first_char != second_char:
            return False
    return True


def is_palindrome_recursive(text, left=None, right=None):
    if left is None and right is None:
        text = text.lower()
        text = re.sub("[^a-zA-Z]+", "", text)
        length = len(text)
        left = 0
        right = length-1
    if left >= right:
        return True
    if text[left] == text[right]:
        return is_palindrome_recursive(text, left+1, right-1)
    else:
        return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
