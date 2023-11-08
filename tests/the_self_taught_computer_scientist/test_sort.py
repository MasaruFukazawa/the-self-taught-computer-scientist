# -*- coding:utf-8 -*-

from the_self_taught_computer_scientist.sort import (
    bubble_sort,
    insertion_sort,
    merge_sort,
)


def test_bubble_sort():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_insertion_sort():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_merge_sort():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
