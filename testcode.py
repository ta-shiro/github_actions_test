#!/usr/bin/env python3
# coding: utdf-8

from typing import List


def test_func(a: int, b: int) -> int:
    return a + b


def test_func2(a: List[int], b: int) -> int:
    return sum(a) * b


if __name__ == '__main__':
    print(test_func(1, 2))
    print(test_func2([1, 2], 3))
    print('Hello.')
