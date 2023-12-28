# -*- coding:utf-8 -*-

from the_self_taught_computer_scientist.queue import Queue


def test_queue():
    queue = Queue()

    queue.enqueue(100)
    queue.enqueue(200)
    queue.enqueue(300)
    queue.enqueue(400)
    queue.enqueue(500)

    assert queue.size == 5

    assert queue.dequeue() == 100
    assert queue.dequeue() == 200
    assert queue.dequeue() == 300
    assert queue.dequeue() == 400
    assert queue.dequeue() == 500

    assert queue.size == 0
