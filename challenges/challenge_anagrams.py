def is_anagram(first_string, second_string):
    ordened_first_string = "".join(merge_sort(first_string.lower()))
    ordened_second_string = "".join(merge_sort(second_string.lower()))

    if len(first_string) == 0 or len(second_string) == 0:
        return (ordened_first_string, ordened_second_string, False)
    elif ordened_first_string == ordened_second_string:
        return (ordened_first_string, ordened_second_string, True)
    else:
        return (ordened_first_string, ordened_second_string, False)


# https://www.freecodecamp.org/portuguese/news/algoritmos-de-ordenacao-explicados-com-exemplos-em-python-java-e-c/
def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(arr, compare=lambda x, y: x < y):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle], compare)
        right = merge_sort(arr[middle:], compare)
        return merge(left, right, compare)
