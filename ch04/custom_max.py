def custom_max(arr):
    if len(arr) == 0:
        raise ValueError("There is no max value for empty arrays")
    first_element = arr[0]
    if len(arr) == 1:
        return first_element
    max_sub_array = custom_max(arr[1:])
    if first_element > max_sub_array:
        return first_element
    return max_sub_array


print("custom_max")
assert custom_max([100, 20, 300, 40]) == 300
try:
    custom_max([])
except ValueError as e:
    assert "There is no max value for empty arrays" in str(e)
assert custom_max([42]) == 42
