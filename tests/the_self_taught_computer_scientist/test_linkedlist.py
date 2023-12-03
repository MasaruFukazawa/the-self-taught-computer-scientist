# -*- coding:utf-8 -*-

from the_self_taught_computer_scientist.linkedlist import LinkedList


def test_add_data_in_linkedlist():
    linkedlist: LinkedList = LinkedList()
    linkedlist.append(100)
    linkedlist.append(200)
    linkedlist.append(300)
    linkedlist.append(400)
    linkedlist.append(500)

    assert linkedlist.datas == [
        100,
        200,
        300,
        400,
        500,
    ]


def test_search_data_in_linkedlist():
    linkedlist: LinkedList = LinkedList()
    linkedlist.append(100)
    linkedlist.append(200)
    linkedlist.append(300)
    linkedlist.append(400)
    linkedlist.append(500)

    assert linkedlist.search(100)
    assert not linkedlist.search(600)


def test_remove_data_in_linkedlist():
    linkedlist: LinkedList = LinkedList()

    linkedlist.append(100)
    linkedlist.append(400)
    linkedlist.append(200)
    linkedlist.append(400)
    linkedlist.append(300)
    linkedlist.append(100)
    linkedlist.append(500)

    linkedlist.remove(100)
    linkedlist.remove(400)
    linkedlist.remove(500)

    assert linkedlist.datas == [
        200,
        300,
    ]


def test_reverse_linkedlist():
    linkedlist: LinkedList = LinkedList()
    linkedlist.append(100)
    linkedlist.append(200)
    linkedlist.append(300)
    linkedlist.append(400)
    linkedlist.append(500)

    linkedlist.reverse()

    assert linkedlist.datas == [
        500,
        400,
        300,
        200,
        100,
    ]


# def test_detect_cycle_linkedlist():
#    linkedlist: LinkedList = LinkedList()
#    linkedlist.append(100)
#    linkedlist.append(200)
#    linkedlist.append(300)
#    linkedlist.append(400)
#    linkedlist.append(500)
#    assert not linkedlist.detect_cycle()
