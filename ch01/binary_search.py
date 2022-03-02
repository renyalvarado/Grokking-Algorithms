def binary_search(ordered_list: list, item) -> int:
    low = 0
    high = len(ordered_list)

    while low <= high:
        mid = (low + high) // 2
        mid_element = ordered_list[mid]
        if mid_element == item:
            return mid
        if mid_element < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
