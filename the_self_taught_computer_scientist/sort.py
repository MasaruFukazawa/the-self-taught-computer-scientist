# -*- coding:utf-8 -*-


def bubble_sort(a_list: list) -> list:
    """
    バブルソート
    """
    loop_size = len(a_list) - 1

    for i in range(loop_size):
        for j in range(loop_size):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

    return a_list


def insertion_sort(a_list: list) -> list:
    """
    挿入ソート
    """
    for i in range(1, len(a_list)):
        value = a_list[i]

        while (i > 0) and (a_list[i - 1] > value):
            a_list[i] = a_list[i - 1]
            i = i - 1

        a_list[i] = value

    return a_list


def merge_sort(a_list: list) -> list:
    """
    マージソート
    """
    if len(a_list) > 1:
        # 引数の配列の要素を2つの配列に分割していく
        # .. 配列の要素数が 1 になるまで再帰的にmerge_sortを呼び出す
        mid = len(a_list) // 2

        # 最終的に 2 // 2 で 1 にあり
        # .. left = a_list[0]
        # .. right = a_list[1]
        left = a_list[:mid]
        right = a_list[mid:]

        # 要素数 1 の場合、さらに分割はせずに値が返る
        # ..  merge_sort(left) の再帰処理が終わったあとで、
        # ..  merge_sort(right)の再帰処理が実行される
        # [5, 4, 3, 2, 1]
        # left のデータ
        # [5, 4]
        # left.left
        # [5]
        # left.right
        # [4]
        # right のデータ
        # [3, 2, 1]
        # right.left
        # [3]
        # right.right
        # [2, 1]
        # right.right.left
        # [2]
        # right.right.right
        # [1]
        merge_sort(left)
        merge_sort(right)

        left_i = 0
        right_i = 0
        a_list_i = 0

        # ここからソート
        # [5] [4]
        # [4, 5]
        # [2] [1]
        # [1, 2]
        # [3] [1, 2]
        # [1, 2, 3]
        # [4, 5], [1, 2, 3]
        # [1, 2, 3, 4, 5]
        # リストは、参照渡しのため、関数に渡して処理が終えると、ソートされたリストが得られる
        while (left_i < len(left)) and (right_i < len(right)):
            if left[left_i] <= right[right_i]:
                a_list[a_list_i] = left[left_i]
                left_i += 1
            else:
                a_list[a_list_i] = right[right_i]
                right_i += 1

            a_list_i += 1

        while left_i < len(left):
            a_list[a_list_i] = left[left_i]
            left_i += 1
            a_list_i += 1

        while right_i < len(right):
            a_list[a_list_i] = right[right_i]
            right_i += 1
            a_list_i += 1

    return a_list
