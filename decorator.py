
def rate_limit(max_call):
    def decorator(func):
        count = 0
        def wrapper(*a, **b):
            nonlocal count
            if count < max_call:
                count += 1
                return func(*a, *b)
            else:
                print("Rate limit exceeded")
        return wrapper
    return decorator
# @rate_limit(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # prints Hello, Alice!
greet("Bob")     # prints Hello, Bob!
greet("Charlie") # prints Hello, Charlie!
greet("David")   # prints Rate limit exceeded
greet("Eve")     # prints Rate limit exceeded


# ================================================================================
# Write a decorator called debug that prints the name of the function being called, along with its arguments and keyword arguments, every time the function is called.

def debug(func):
    def wrapper(*a, **b):
        print(f"Calling {func.__name__} with args: {a}, kwargs: {b}")
        return func(*a, **b)
    return wrapper

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice", greeting="Hi")

# ================================================================================
# Write a decorator called timer that measures how long a function takes to run, and prints the time in seconds.
import time

def timer(func):
    def wrapper(*a, **b):
        t = time.time()
        result = func(*a, **b)
        print("Time:", time.time() - t)
        return result
    return wrapper

@timer
def slow_function():
    for _ in range(1000000):
        pass

slow_function()
