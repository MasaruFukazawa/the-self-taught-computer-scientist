# -*- coding:utf-8 -*-

from the_self_taught_computer_scientist.palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome("Hannah")
    assert not is_palindrome("Hannaa")
