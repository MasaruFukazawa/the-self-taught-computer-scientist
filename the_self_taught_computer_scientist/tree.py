# -*- coding:utf-8 -*-

from __future__ import annotations

from typing import Optional


class BinaryTree:
    def __init__(self, value: int) -> None:
        self.key: int = value
        self.left_child: Optional[BinaryTree] = None
        self.right_child: Optional[BinaryTree] = None

    def insert_left(self, value: int) -> None:
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree: BinaryTree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value: int) -> None:
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree: BinaryTree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def breadth_first_search(self, n: int):
        """幅優先探索"""
        current: list[BinaryTree] = [self]
        next: list[BinaryTree] = []

        while current:
            for node in current:
                if node.key == n:
                    return True

                if node.left_child:
                    next.append(node.left_child)

                if node.right_child:
                    next.append(node.right_child)

            current = next
            next = []

        return False

    def invert(self):
        """2分木を反転させる"""
        current: list[BinaryTree] = [self]
        next: list[BinaryTree] = []

        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)

                if node.right_child:
                    next.append(node.right_child)

                tmp: Optional[BinaryTree] = node.left_child

                node.left_child = node.right_child
                node.right_child = tmp

            current = next
            next = []


def preoder(tree):
    """行きがけ順走査"""
    if tree:
        print(tree.key)
        preoder(tree.left_child)
        preoder(tree.right_child)


def postorder(tree):
    """帰りがけ順走査"""
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)


def inorder(tree):
    """通りがけ順走査"""
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)


if __name__ == "__main__":
    tree = BinaryTree(2)
    tree.insert_left(1)
    tree.insert_right(3)

    preoder(tree)
    postorder(tree)
    inorder(tree)
