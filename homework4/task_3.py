import datetime
import functools


def log_calls(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now()
            log_entry = (
                f"{current_time} - {func.__name__} - args: {args}, kwargs: {kwargs}\n"
            )
            with open(filename, "a") as log_file:
                log_file.write(log_entry)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_calls("function_calls.log")
def example_function(a, b, c=None):
    return a + b if c is None else a + b + c


print(example_function(1, 2))
print(example_function(1, 2, c=3))
