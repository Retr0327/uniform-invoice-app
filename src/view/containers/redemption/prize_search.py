from typing import List, Literal, Union


def sort_tuple(array: List):
    """The sort_tuple sorts a list of tuples based on the second argument of the tuple."""
    array.sort(key=lambda x: int(x[1]))
    return array


async def binary_search(array: List, target) -> Union[int, Literal[False]]:
    array = sort_tuple(array)
    first = 0
    last = len(array) - 1

    while first <= last:
        mid = (first + last) // 2
        if array[mid][1] == target:
            return array[mid][0]
        elif int(target) < int(array[mid][1]):
            last = mid - 1
        else:
            first = mid + 1

    return False
