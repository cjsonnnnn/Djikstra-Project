import pytest
from keterpencilan.dijkstra import shortest_path
from keterpencilan.adding_csv_data import create_graph_tidak_berarah

def test_shortest_path_with_empty_node():
    class Empty_Graph:
        def __init__(self):
            self.internal_array = [[]]

    assert shortest_path(1, Empty_Graph()) == None, "TEST FAILED"

def test_shortest_path_with_a_node():
    class A_Graph:
        def __init__(self):
            self.internal_array = [[0]]

    assert shortest_path(1, A_Graph()) == None, "TEST FAILED"

def test_calculate_keterpencilan():
    class Graph:
        def __init__(self):
            self.internal_array = create_graph_tidak_berarah("DaftarJalan.csv", "DaftarKota.csv")

    maps = Graph()
    FROM = 0

    assert shortest_path(FROM, maps) == {0: 0, 1: 1.0, 2: 3.0, 3: 4.0, 4: 13.0}, "TEST FAILED"