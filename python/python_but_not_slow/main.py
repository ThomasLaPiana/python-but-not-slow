"""
Basic webserver to demonstrate using Python vs. Rust, from a Python webserver,
for computationally intensive tasks.
"""

from litestar import Litestar, get

app = Litestar()


@get("/python/{num:int}")
def index_python(num: int) -> str:
    """
    Basic endpoint that does a computationally intensive task in Python.
    """
    return str(calculate_fibonacci(num))


@get("/rust")
def index_rust() -> str:
    """
    Basic endpoint that does a computationally intensive task in Rust.
    """
    return "Hello, world!"


def calculate_fibonacci(num: int) -> int:
    """
    Calculate the Fibonacci number for a given number.
    """
    num1 = 0
    num2 = 1
    next_number = num2
    count = 1

    while count <= num:
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2

    return num2
