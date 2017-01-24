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
    base_ten = 0
    length = len(str_num)
    for i in range(0, length):
        try:
            digit_value = int(str_num[i])
            base_ten += pow(base, length-1-i) * digit_value
        except ValueError:
            # Must be a non digit
            # Asumption - all letters will be lower case
            # Subract 87 because ascii value of 'a' is 97
            char_to_value = ord(str_num[i].lower()) - 87
            # print 'Yikes, the ord value is: ', char_to_value
            base_ten += pow(base, length-1-i) * char_to_value

    # print 'str rep: ', str_num, ' base: ', base
    # print 'convert: ', base_ten
    return base_ten

def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    num_base = 0

    # Step 1 find the largest power of the base that 'fits' in the num
    temp_num = 1
    highest_power = 0
    while temp_num <= num:
        highest_power += 1
        temp_num = temp_num * base

    highest_power -= 1

    print 'Given base 10 num: ', num
    print 'Convert to base: ', base
    print 'highest power: ', highest_power

    result = ''
    current_power = highest_power
    while num >= 1:
        # if num == 1:
        #     result = result.ljust(highest_power,'0')
        #     result += str(1)
        #     break
        i = 1
        highest_value = pow(base, current_power) * (base - i)
        print 'high val: ', highest_value
        while num - highest_value < 0:
            i += 1
            highest_value = pow(base, current_power) * (base - i)

        print 'current result: ', (base-i)
        print 'highest_value: ', highest_value
        if (base - i) < 10:
            result += str((base - i))
        else:
            result += chr((base-i) + 87)

        num -= highest_value
        current_power -= 1

    result = result.ljust(highest_power+1,'0')

    print 'result: ', result
    return result







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
