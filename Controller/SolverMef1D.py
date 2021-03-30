import numpy as np
from Domain.Mesh import Mesh
from Utils import gauss_points, weigths

class SolverMef1D:
    def _build_global_matrix(self, mesh: Mesh) -> np.array:
        global_matrix = np.zeros([self.number_nodes, self.number_nodes])
        for element in range(mesh.elements_number):
            nodes = mesh.get_nodes_of_element(element)
            for node_i in nodes:
                for node_j in nodes:
                    for gauss_point, weight in zip(gauss_points, weigths):
                        global_matrix[node_i.id, node_j.id]  += weight * node_i.shape_function(gauss_point) \
                                                                * node_j.shape_function(gauss_point) * 1/self.number_nodes
        return global_matrix

    def _build_elementary_vector(self, mesh: Mesh, func) -> np.array:
        fg = np.zeros(self.number_nodes)
        for element in range(mesh.elements_number):
            nodes = mesh.get_nodes_of_element(element)
            for node_i in nodes:
                for gauss_point, weight in zip(gauss_points, weigths):
                    fg[node_i.id] += weight * node_i.shape_function(gauss_point) \
                                     * func(gauss_point)
        return fg

    def __init__(self, mesh: Mesh, func):
        self.number_nodes = mesh.nodes_number
        self.global_matrix = self._build_global_matrix(mesh)
        self.elementary_vector = self._build_elementary_vector(mesh, func)
        np.set_printoptions(precision=3)
        print(self.global_matrix)
        print(self.elementary_vector)

    def solver_mef(self):
        return np.linalg.solve(self.global_matrix, self.elementary_vector)