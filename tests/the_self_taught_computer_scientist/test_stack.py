# -*- coding:utf-8 -*-

from the_self_taught_computer_scientist.stack import Stack


def test_push_in_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.size() == 5


def test_pop_from_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.pop() == 4


def test_is_empty():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.pop()
    stack.pop()
    stack.pop()

    assert stack.is_empty()


def test_peek_in_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.peek() == 5
