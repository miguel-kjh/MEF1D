from Domain.Node import Node
from Utils import shape_function, shape_function_derivative
import numpy as np

class Mesh:
    """
    Construye la malla en 1D
    """

    def __init__(self, elements_number: int, a: int = 0, b: int = 1):
        # Restriciones
        assert elements_number > 1
        assert a < b

        self.elements_number = elements_number
        self.he = (b-a)/self.elements_number
        self.interval = np.arange(a, b, self.he)
        self.interval = np.append(self.interval, b)
        self.nodes = []
        self._build_mesh()

    def _build_mesh(self):
        """
        Construye la malla,añade tres nodos a cada elementos porque usamos basas cuadradas
        :return:
        """
        id = 0
        for interval_index, element in enumerate(range(self.elements_number)):
            sub_interval = self.interval[interval_index:interval_index+2]
            """
            En cada nodo se almacena el id, el elemento al que pertenece, las funciones de formas y el intervalo donde
            pertence.
            """
            self.nodes.append(Node(id, element, shape_function[0], shape_function_derivative[0], sub_interval))
            id += 1
            self.nodes.append(Node(id, element, shape_function[1], shape_function_derivative[1], sub_interval))
            id += 1
            self.nodes.append(Node(id, element, shape_function[2], shape_function_derivative[2], sub_interval))
        self.nodes_number = id + 1

    def get_nodes_of_element(self, element: int) -> list:
        """
        Devuelve los nodos pertenecientes a un elmento finito
        :param element: int
        :return: list
        """
        return [node for node in self.nodes if element == node.element]

    def get_points(self) -> list:
        """
        Devuelve una lista con todos los puntos de la malla
        :return: list
        """
        points = []
        for i in range(len(self.interval) - 1):
            points.append(self.interval[i])
            points.append((self.interval[i+1] - self.interval[i])/2 + self.interval[i])
        points.append(self.interval[-1])
        return points