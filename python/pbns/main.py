"""
Basic webserver to demonstrate using Python vs. Rust, from a Python webserver,
for computationally intensive tasks.
"""

import logging

from litestar import Litestar, get

from pbns import _pbns

logger = logging.getLogger(__name__)


@get("/python/{num:int}")
async def index_python(num: int) -> dict[str, int]:
    """
    Basic endpoint that does a computationally intensive task in Python.
    """
    try:
        result = fibonacci_python(num)
        return {"detail": result}
    except Exception as e:
        logger.error(e)
        return {"error": str(e)}


@get("/rust/{num:int}")
async def index_rust(num: int) -> dict[str, int]:
    """
    Basic endpoint that does a computationally intensive task in Rust.
    """
    return {"detail": _pbns.fibonacci(num)}


def fibonacci_python(num: int) -> int:
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


app = Litestar(route_handlers=[index_python, index_rust])
