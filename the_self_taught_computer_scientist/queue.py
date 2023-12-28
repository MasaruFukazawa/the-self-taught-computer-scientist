# -*- coding:utf-8 -*-

from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, data: int, next: Optional[Node] = None) -> None:
        self.__data: int = data
        self.__next: Optional[Node] = next

    @property
    def data(self) -> int:
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node: Node):
        self.__next = node


class Queue:
    def __init__(self) -> None:
        self.__front: Optional[Node] = None
        self.__rear: Optional[Node] = None
        self.__size: int = 0

    def enqueue(self, item: int) -> None:
        self.__size += 1

        node = Node(item)

        if self.__rear is None:
            self.__front = node
            self.__rear = node
        else:
            self.__rear.next = node
            self.__rear = node

    def dequeue(self) -> int:
        if self.__front is None:
            raise IndexError("pop from empty queue")

        self.__size -= 1

        temp = self.__front

        self.__front = self.__front.next

        if self.__front is None:
            self.__rear = None

        return temp.data

    @property
    def size(self):
        return self.__size
