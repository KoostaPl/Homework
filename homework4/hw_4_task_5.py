def cache(func):
    cache_storage = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key in cache_storage:
            return cache_storage[key]
        else:
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return wrapper


@cache
def number_pow(n, x):
    print(f"Число {n} в степени {x} равняется: ")
    return n**x


print(number_pow(2, 5))
print(number_pow(3, 8))
print(number_pow(15, 5))
