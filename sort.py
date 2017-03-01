import math


def bubble_sort(a, comparison):
    is_sorted = False
    length = len(a)
    while not is_sorted:
        maybe_sorted = True
        for i in range(0, length-1):
            if not comparison(a[i], a[i+1]):
                maybe_sorted = False
                a[i], a[i+1] = a[i+1], a[i]
        is_sorted = maybe_sorted
    return a


def selection_sort(a, comparison, sorted_list=[]):
    # Currently a is destroyed in the process
    if a == []:
        return sorted_list
    length = len(a)
    next_element_index = 0
    for i in range(0, length):
        if not comparison(a[next_element_index], a[i]):
            next_element_index = i
    sorted_list.append(a[next_element_index])
    del a[next_element_index]
    return selection_sort(a, comparison, sorted_list)


def insertion_sort(a):
    result = []
    length = 0
    for item in a:
        for i in range(0, len(result)+1):
            if i == length:
                result.append(item)
                length += 1
                break
            elif item > result[i]:
                result.insert(i, item)
                length += 1
                break
    return result


def counting_sort(a):
    pass


def bucket_sort(a):
    length = len(a)
    if length < 1:
        return a
    max_element = a[0]
    for item in a:
        if item > max_element:
            max_element = item

    buckets_count = int(math.ceil(length / 2.0))
    buckets = []
    for i in range(0, buckets_count):
        buckets.append([])

    for item in a:
        bucket_index = item / buckets_count
        buckets[bucket_index].append(item)

    result = []
    for bucket in buckets:
        bucket = bubble_sort(bucket, lambda x, y: x > y)

    for i in range(0, buckets_count):
        cur_bucket = buckets[buckets_count - 1 - i]
        for i in cur_bucket:
            result.append(i)
    return result


def merge_sort(a):
    # break list down into sublists!
    list_of_arrays = []
    for item in a:
        list_of_arrays.append([item])

    while len(list_of_arrays) > 1:
        print(list_of_arrays)
        new_list_of_arrays = []
        length_list = len(list_of_arrays)

        for i in range(0, length_list-1, 2):
            new_list_of_arrays.append(merge(list_of_arrays[i], list_of_arrays[i+1]))
        if length_list % 2 == 1:
            # Grab last element and append
            new_list_of_arrays.append(list_of_arrays[length_list-1])
        list_of_arrays = new_list_of_arrays

    return list_of_arrays


def merge(a, b):
    result = []
    length_a = len(a)
    length_b = len(b)

    cur_a_index = 0
    cur_b_index = 0

    while cur_a_index < length_a and cur_b_index < length_b:
        cur_a = a[cur_a_index]
        cur_b = b[cur_b_index]
        if cur_a > cur_b:
            result.append(cur_a)
            cur_a_index += 1
        elif cur_a == cur_b:
            result.append(cur_a)
            cur_a_index += 1
        elif cur_a < cur_b:
            result.append(cur_b)
            cur_b_index += 1

    if cur_b_index < length_b:
        result.extend(b[cur_b_index:])
    if cur_a_index < length_a:
        result.extend(a[cur_a_index:])

    return result




array = [1, 2, 3, 4, 5]
print(bubble_sort(array, lambda x, y: x > y))
print(selection_sort(array, lambda x, y: x > y))

array = [1, 2, 3, 4, 5]
print(insertion_sort(array))

array = [1, 2, 3, 4, 5]
print(bucket_sort(array))

array = [4, 2, 3, 1, 5]
print(merge_sort(array))

array = [4, 2, 3, 1, 5]
print(merge_sort(array))

array = [4, 2, 3, 1, 5]
print(merge_sort(array))

array = [58, 25, 3, 7, 4, 9, 4, 3, 6]
print(merge_sort(array))
