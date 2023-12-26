# -*- coding:utf-8 -*-

from __future__ import annotations

from typing import Optional


class Stack:
    def __init__(self) -> None:
        self.items: list[int] = []

    def push(self, data: int) -> None:
        self.items.append(data)

    def pop(self) -> int:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def peek(self) -> int:
        return self.items[-1]


class Node:
    def __init__(self, data: int) -> None:
        self.__data: int = data
        self.__next: Optional[Node] = None

    @property
    def data(self) -> int:
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node: Node):
        self.__next = node


class ListStack:
    def __init__(self) -> None:
        self.__head: Optional[Node] = None

    def push(self, data: int) -> None:
        node: Node = Node(data)

        if self.__head is None:
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node

    def pop(self) -> int:
        if self.__head is None:
            raise IndexError("pop from empty stack")

        popped_node: Node = self.__head

        self.__head = self.__head.next

        return popped_node.data

    def size(self) -> int:
        if self.is_empty():
            return 0

        node: Optional[Node] = self.__head
        count: int = 0

        while node:
            count += 1
            node = node.next

        return count

    def is_empty(self) -> bool:
        if self.__head is None:
            return True

        return False

    def peek(self) -> int:
        if self.__head is None:
            raise IndexError("pop from empty stack")

        return self.__head.data


class MinStack:
    def __init__(self) -> None:
        self.__main: list[int] = []
        self.__min: list[int] = []

    def push(self, data: int) -> None:

        if len(self.__main) == 0:
            self.__min.append(data)
        elif data <= self.__min[-1]:
            self.__min.append(data)
        else:
            self.__min.append(self.__min[-1])

        self.__main.append(data)

    def pop(self) -> int:
        self.__min.pop()
        return self.__main.pop()
