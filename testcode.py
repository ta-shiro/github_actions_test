from typing import List, Union

def test_func(a: int, b: int) -> int:
    return a + b

def test_func2(a: list, b: int) -> int:
    return sum(a) * b