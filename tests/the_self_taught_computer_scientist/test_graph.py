# -*- coding:utf-8 -*-

from the_self_taught_computer_scientist.graph import Graph


def test_graph():
    graph = Graph()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    graph.add_edge("A", "B", 1)
    graph.add_edge("B", "C", 10)

    # vertex_a = graph.get_vertex("A")
    # vertex_b = graph.get_vertex("B")
