def custom_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + custom_sum(arr[1:])


print("custom_sum")
assert custom_sum([10, 20, 30, 40]) == 100
assert custom_sum([]) == 0
assert custom_sum([42]) == 42
