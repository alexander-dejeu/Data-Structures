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


# def optimized_insertion_sort(a, comparison):
#     result = []
#     length = 0
#     for item in a:
#         for i in range(0, len(result)+1):
#             if i == length:
#                 result.append(item)
#                 length += 1
#                 break
#             elif item > result[i]:
#                 result.insert(i, item)
#                 length += 1
#                 break
#     return result


array = [1, 2, 3, 4, 5]
print(bubble_sort(array, lambda x, y: x > y))
print(selection_sort(array, lambda x, y: x > y))

array = [1, 2, 3, 4, 5]
print(insertion_sort(array))

array = [1, 2, 3, 4, 5]
print(bucket_sort(array))
