from Domain.Node import Node
from Utils import shape_function, shape_function_derivative
import numpy as np

# Hacer que más de un nodo tenga el mismo ID
class Mesh:

    def _build_mesh(self):
        id = 0
        for interval_index, element in enumerate(range(self.elements_number)):
            sub_interval = self.interval[interval_index:interval_index+2]
            self.nodes.append(Node(id, element, shape_function[0], shape_function_derivative[0], sub_interval))
            id += 1
            self.nodes.append(Node(id, element, shape_function[1], shape_function_derivative[1], sub_interval))
            id += 1
            self.nodes.append(Node(id, element, shape_function[2], shape_function_derivative[2], sub_interval))
        self.nodes_number = id + 1

    def __init__(self, elements_number: int, a: int = 0, b: int = 1):
        self.elements_number = elements_number
        self.interval = np.arange(a, b, (b-a)/self.elements_number)
        self.interval = np.append(self.interval, b)
        self.nodes = []
        self._build_mesh()

    def get_nodes_of_element(self, element: int):
        return [node for node in self.nodes if element == node.element]