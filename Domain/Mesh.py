from Domain.Node import Node
from Utils import shape_functions

# Hacer que más de un nodo tenga el mismo ID
class Mesh:

    def _bild_mesh(self):
        self.nodes.append(Node(0, 0, shape_functions[0]))

        id = 1
        for element in range(self.elements_number):
            for shape_function in shape_functions[1:]:
                if id % 2 == 0 and element + 1 < self.elements_number:
                    self.nodes.append(
                        Node(id, (element, element + 1), shape_function)
                    )
                else:
                    self.nodes.append(
                        Node(id, element, shape_function)
                    )
                id += 1

    def __init__(self, elements_number: int):
        self.elements_number = elements_number
        self.nodes = []
        self._bild_mesh()

    def _check_element(self, node_element: int, element: int) -> bool:
        if type(node_element) == tuple:
            return element in node_element
        else:
            return element == node_element

    def get_nodes_of_element(self, element: int):
        return [node for node in self.nodes if self._check_element(node.element, element)]