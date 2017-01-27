#!python
import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    try:
        cur_value = array[index]
        if cur_value == item:
            return index
        else:
            return linear_search_recursive(array, item, index+1)
    except IndexError:
        return None

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # Init tried with just a single var but it caused problems with jumping one
    # bellow and above the number forever :/ Changed to two vars
    first = 0
    last = len(array) - 1
    valid = True
    while valid:
        mid_point = int((first + last) / 2)
        if first > last:
            return None
        if array[mid_point] == item:
            return mid_point
        elif array[mid_point] > item:
            last = mid_point - 1
        else:
            first = mid_point + 1
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below


def binary_search_recursive(array, item, left=None, right=None):
    # Similar to above if the max crosses the min you are done, not found
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if right < left:
        return None
    else:
        mid_point = int((left + right) / 2)
        if array[mid_point] == item:
            return mid_point
        elif array[mid_point] > item:
            right = mid_point - 1
        else:
            left = mid_point + 1
        return binary_search_recursive(array, item, left, right)




    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below
