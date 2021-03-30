from Domain.Node import Node
from Utils import shape_functions

# Hacer que más de un nodo tenga el mismo ID
class Mesh:

    def _build_mesh(self):
        id = 0
        for element in range(self.elements_number):
            self.nodes.append(Node(id, element, shape_functions[0]))
            id += 1
            self.nodes.append(Node(id, element, shape_functions[1]))
            id += 1
            self.nodes.append(Node(id, element, shape_functions[2]))
        self.nodes_number = id + 1

    def __init__(self, elements_number: int):
        self.elements_number = elements_number
        self.nodes = []
        self._build_mesh()

    def get_nodes_of_element(self, element: int):
        return [node for node in self.nodes if element == node.element]