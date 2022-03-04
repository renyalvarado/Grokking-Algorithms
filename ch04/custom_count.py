def custom_count(arr):
    if len(arr) == 0:
        return 0
    return 1 + custom_count(arr[1:])


print("custom_count")
assert custom_count([10, 20, 30, 40]) == 4
assert custom_count([]) == 0
assert custom_count([42]) == 1
