# -*- coding:utf-8 -*-


def is_palindrome(s1: str) -> bool:
    _s1: str = s1.lower()

    return _s1 == _s1[::-1]
