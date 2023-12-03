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


class LinkedList:
    def __init__(self) -> None:
        self.__head: Optional[Node] = None

    @property
    def head(self) -> Optional[Node]:
        return self.__head

    @head.setter
    def head(self, node: Node):
        self.__head = node

    @property
    def datas(self) -> list[int]:
        data_list: list = []
        current: Optional[Node] = self.head

        while current:
            data_list.append(current.data)
            current = current.next

        return data_list

    def append(self, data: int) -> None:
        if not self.head:
            self.head = Node(data)
            return

        current: Node = self.head

        while current.next:
            current = current.next

        current.next = Node(data)

    def search(self, target: int) -> bool:
        current: Optional[Node] = self.head

        while current:
            if current.data == target:
                return True
            current = current.next

        return False

    def remove(self, target: int) -> None:
        if not self.head:
            return

        previous: Optional[Node] = self.head
        current: Optional[Node] = self.head.next

        if previous and current:
            while current:
                if current.data == target:
                    previous.next = current.next
                previous = current
                current = current.next

        if self.head.data == target:
            self.head = self.head.next
            return

    def reverse(self) -> None:
        if not self.head:
            return

        if not self.head.next:
            return

        current: Optional[Node] = self.head
        previous: Optional[Node] = None

        while current:
            next: Optional[Node] = current.next

            current.next = previous
            previous = current

            current = next

        self.head = previous

    def detect_cycle(self) -> bool:
        if not self.head:
            return False

        slow: Node = self.head
        fast: Node = self.head

        while True:
            try:
                slow = slow.next
                fast = fast.next.next
            except AttributeError:
                return False

            if slow is fast:
                return True
