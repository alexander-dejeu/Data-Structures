#!python

import string


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36
    # Step 1 see how many times it is divided by self
    sum = 0
    length = len(str_num)
    for i in range(0, length):
        try:
            digit_value = int(str_num[i])
            sum += pow(base, length-1-i) * digit_value
        except ValueError:
            # Must be a non digit
            # Asumption - all letters will be lower case
            # Subract 87 because ascii value of 'a' is 97
            char_to_value = ord(str_num[i].lower()) - 87
            print 'Yikes, the ord value is: ', char_to_value
            sum += pow(base, length-1-i) * char_to_value

    print 'str rep: ', str_num, ' base: ', base
    print 'convert: ', sum
    return sum

def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    # TODO: Encode number


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
