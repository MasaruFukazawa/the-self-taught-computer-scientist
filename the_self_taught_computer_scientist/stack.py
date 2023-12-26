# -*- coding:utf-8 -*-

from __future__ import annotations


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
