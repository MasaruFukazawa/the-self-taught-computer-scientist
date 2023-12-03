# -*- coding:utf-8 -*-

from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, data: int, next: Optional[Node] = None) -> None:
        self.data: int = data
        self.next: Optional[Node] = next


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

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
            return None

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

    # def detect_cycle(self) -> None:
    #    if not self.head:
    #        return
    #    slow = self.head
    #    fast = self.head
    #    while True:
    #        try:
    #            slow = slow.next
    #            fast = fast.next.next
    #            if slow is fast:
    #                return True
    #        except Exception:
    #            return False
