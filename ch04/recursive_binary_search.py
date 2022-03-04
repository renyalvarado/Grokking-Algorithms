def recursive_binary_search(ordered_list: list, item) -> int:
    size = len(ordered_list)
    if size == 0:
        return -1

    mid = size // 2
    mid_element = ordered_list[mid]
    if mid_element == item:
        return mid
    if mid_element < item:
        return recursive_binary_search(ordered_list[mid + 1:], item)
    else:
        return recursive_binary_search(ordered_list[:mid], item)


print("recursive_binary_search")
my_list = [1, 3, 5, 7, 9]
assert recursive_binary_search(my_list, 3) == 1
assert recursive_binary_search(my_list, 4) == -1

