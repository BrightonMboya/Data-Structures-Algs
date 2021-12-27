def get_smaller_than_or_equal_to(array, k):
    if array == []:
        return []
    elif array[0] <= k:
        return [array[0]] + get_smaller_than_or_equal_to(array[1:], k)
    else:
        return get_smaller_than_or_equal_to(array[1:], k)

get_smaller_than_or_equal_to([10, 7, 1, 6, 3], 5)