import sys


def get_full_binary(number, max_digits):
    # https://docs.python.org/3/library/platform.html#platform.architecture
    size = 28
    prefix = "1" if number < 0 else "0"
    binary_template = f"{{i:0{max_digits}}}: {prefix}{{i:0{size}b}}"
    return binary_template.format(i=abs(number))


for i in range(-10, 10):
    print(get_full_binary(i, 3))


class CustomDictionary:

    def __init__(self, hash_function=hash) -> None:
        self._dict_size = 8
        self._hash_function = hash_function
        self._hash_buckets = [[] for i in range(self._dict_size)]

    def _get_bucket(self, key):
        hash_key = self._hash_function(key)
        index = hash_key % self._dict_size
        print(f"{key}: {hash_key}, {index}")
        return self._hash_buckets[index]

    def insert_element(self, key, value):
        bucket = self._get_bucket(key)
        bucket.append((key, value), )

    def __setitem__(self, key, value):
        self.insert_element(key, value)

    def get_element(self, key):
        bucket = self._get_bucket(key)
        for k, v in bucket:
            if k == key:
                return v
        return None

    def __str__(self):
        return f"<CustomDictionary {self._hash_buckets}>"


def hash_1(x):
    return 1


def hash_length(x):
    return len(x)


def hash_first_element(x):
    return ord(x[0])


def print_custom_array(hash_function):
    print()
    print("*" * 80)
    print(hash_function.__name__)
    custom_dict = CustomDictionary(hash_function)
    custom_dict["Australia"] = "Canberra"
    custom_dict["Brasil"] = "Brasilia"
    custom_dict["Egypt"] = "Cairo"
    custom_dict["Italy"] = "Rome"
    custom_dict["China"] = "Beijing"
    custom_dict["Argentina"] = "Buenos Aires"
    custom_dict["Colombia"] = "Bogotá"
    custom_dict["France"] = "Paris"
    print(custom_dict)
    print()
    print(custom_dict.get_element("China"))
    print(custom_dict.get_element("Greece"))


print({i: sys.getsizeof(i) for i in range(-10, 10)})

for f in [hash, hash_1, hash_length, hash_first_element]:
    print_custom_array(f)
