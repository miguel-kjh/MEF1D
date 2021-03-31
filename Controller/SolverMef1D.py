import numpy as np
from Domain.Mesh import Mesh
from Utils import gauss_points, weigths, G, FACTOR


class SolverMef1D:

    def __init__(self, mesh: Mesh, func, neumann_cond: list = [None,None], dirichlet_cond: list = [None,None]):
        self.number_nodes = mesh.nodes_number
        self.mesh = mesh
        self.global_matrix = self._build_global_matrix(mesh)
        self.elementary_vector = self._build_elementary_vector(mesh, func)
        self._apply_neumann_cond(neumann_cond)
        self._apply_dirichlet_cond(dirichlet_cond)
        self.solution = np.linalg.solve(self.global_matrix, self.elementary_vector)

    def _build_global_matrix(self, mesh: Mesh) -> np.array:
        global_matrix = np.zeros([self.number_nodes, self.number_nodes])
        for element in range(mesh.elements_number):
            nodes = mesh.get_nodes_of_element(element)
            for node_i in nodes:
                for node_j in nodes:
                    for gauss_point, weight in zip(gauss_points, weigths):
                        global_matrix[node_i.id, node_j.id] += weight * node_i.shape_function_derivative(gauss_point) \
                                                                * node_j.shape_function_derivative(gauss_point) * FACTOR
        return global_matrix

    def _build_elementary_vector(self, mesh: Mesh, func) -> np.array:
        fg = np.zeros(self.number_nodes)
        for element in range(mesh.elements_number):
            nodes = mesh.get_nodes_of_element(element)
            for node_i in nodes:
                for gauss_point, weight in zip(gauss_points, weigths):
                    fg[node_i.id] += weight * node_i.shape_function(gauss_point) \
                                     * func((gauss_point + 3*sum(node_i.interval))* FACTOR) * FACTOR
        return fg

    def _apply_neumann_cond(self, neumann_cond):
        self.elementary_vector[0] -= neumann_cond[0] if neumann_cond[0] is not None else 0
        self.elementary_vector[-1] -= neumann_cond[1] if neumann_cond[1] is not None else 0

    def _apply_dirichlet_cond(self, dirichlet_cond):
        if dirichlet_cond[0] is not None:
            self.global_matrix[0][0]  = G
            self.elementary_vector[0] = G*dirichlet_cond[0]

        if dirichlet_cond[1] is not None:
            self.global_matrix[-1][-1] = G
            self.elementary_vector[-1] = G*dirichlet_cond[1]

    def solver_mef(self, x) -> float:
        result = 0
        points = self.mesh.get_points()
        for i in range(len(self.solution)):
            fi = 1
            for j in range(len(points)):
                if i != j:
                    fi *= (x - points[j]) / (points[i] - points[j])
            result += self.solution[i] * fi
        return result