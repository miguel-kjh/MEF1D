from Domain.Node import Node
from Utils import shape_functions

class Mesh:

    def _bild_mesh(self):
        self.nodes.append(Node(0, 0, shape_functions[0]))

        id = 1
        for element in range(self.elements_number):
            for shape_function in shape_functions[1:]:
                self.nodes.append(
                    Node(id, element, shape_function)
                )
                id += 1

    def __init__(self, elements_number: int):
        self.elements_number = elements_number
        self.nodes = []
        self._bild_mesh()