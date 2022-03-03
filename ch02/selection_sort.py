def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        element = arr[i]
        if element < smallest:
            smallest = element
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    elements = []
    while len(arr) > 0:
        smallest_index = find_smallest(arr)
        elements.append(arr.pop(smallest_index))
    return elements


print(selection_sort([5, 3, 6, 2, 10]))
