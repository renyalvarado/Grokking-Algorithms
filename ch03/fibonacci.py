import functools
import time


def fibonacci(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)


@functools.lru_cache
def fibonacci_memoize(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibonacci_memoize(x - 1) + fibonacci_memoize(x - 2)


for f in [fibonacci, fibonacci_memoize]:
    print("*" * 80)
    start = time.perf_counter()
    for i in range(35):
        print(f"{f.__name__}({i}): {f(i)}")
    end = time.perf_counter()
    print(f"Execution time: {(end - start):.3f} sec")
    print("*" * 80)
    print()
