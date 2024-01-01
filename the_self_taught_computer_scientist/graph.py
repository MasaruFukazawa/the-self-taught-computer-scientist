# -*- coding:utf-8 -*-

from __future__ import annotations

from typing import Optional


class Vertex:
    def __init__(self, key: str) -> None:
        self.key = key
        self.connections: dict[Vertex, int] = {}

    def add_adj(self, vertex: Vertex, weight: int = 0) -> None:
        self.connections[vertex] = weight

    def get_connections(self) -> list[Vertex]:
        return list(self.connections.keys())

    def get_weight(self, vertex: Vertex) -> int:
        return self.connections[vertex]


class Graph:
    def __init__(self) -> None:
        self.vertex_dict: dict[str, Vertex] = {}

    def add_vertex(self, key):
        new_vertex: Vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex

    def get_vertex(self, key: str) -> Optional[Vertex]:
        if key in self.vertex_dict:
            return self.vertex_dict[key]
        return None

    def add_edge(self, f: str, t: str, weight: int = 0) -> None:
        if f not in self.vertex_dict:
            self.add_vertex(f)

        if t not in self.vertex_dict:
            self.add_vertex(t)

        self.vertex_dict[f].add_adj(self.vertex_dict[t], weight)
