import numpy as np
from Domain.Mesh import Mesh
from Utils import gauss_points, weigths, G

class SolverMef1D:

    def _check_boundary_conditions(self, dirichlet_cond) -> bool:
        return dirichlet_cond[0] != None or dirichlet_cond[1] != None


    def __init__(self, mesh: Mesh, func, neumann_cond: list = [None,None],
                 dirichlet_cond: list = [None,None], verbose: bool = False):

        if not self._check_boundary_conditions(dirichlet_cond):
            raise RuntimeError("missing specification of boundary conditions")

        # datos para resolver el MEF
        self.number_nodes = mesh.nodes_number
        self.jacobiano = 1 / 2 * mesh.he
        self.jacobiano_inv = 1/self.jacobiano
        self.mesh = mesh

        # Construimos la matriz y el vector
        self.global_matrix = self._build_global_matrix(mesh)
        self.elementary_vector = self._build_elementary_vector(mesh, func)

        # Aplicamos condiciones de controno
        self._apply_neumann_cond(neumann_cond)
        self._apply_dirichlet_cond(dirichlet_cond)

        # Resolvemos el sistema
        self.solution = np.linalg.solve(self.global_matrix, self.elementary_vector)

        if verbose:
            np.set_printoptions(precision=3)
            print("Matriz global")
            print(self.global_matrix)
            print("Vector elemental")
            print(self.elementary_vector)
            print("Solución")
            print(self.solution)

    def _build_global_matrix(self, mesh: Mesh) -> np.array:
        """
        Construye la matriz global
        :param mesh: Mesh
        :return: np.array
        """
        global_matrix = np.zeros([self.number_nodes, self.number_nodes])
        for element in range(mesh.elements_number):
            nodes = mesh.get_nodes_of_element(element)
            for node_i in nodes:
                for node_j in nodes:
                    for gauss_point, weight in zip(gauss_points, weigths):
                        # Se utiliza el id para hacer el ensamblaje
                        global_matrix[node_i.id, node_j.id] += weight * self.jacobiano_inv * node_i.shape_function_derivative(gauss_point) \
                                                                * node_j.shape_function_derivative(gauss_point)
        return global_matrix

    def _build_elementary_vector(self, mesh: Mesh, func) -> np.array:
        """
        Construye el vector elemental
        :param mesh: Mesh
        :param func: función
        :return: np.array
        """
        fg = np.zeros(self.number_nodes)
        for element in range(mesh.elements_number):
            nodes = mesh.get_nodes_of_element(element)
            for node_i in nodes:
                for gauss_point, weight in zip(gauss_points, weigths):
                    # Se utiliza el id para hacer el ensamblaje
                    fg[node_i.id] += weight * node_i.shape_function(gauss_point) \
                                     * func((mesh.he*gauss_point + sum(node_i.interval))/2) * self.jacobiano
        return fg

    def _apply_neumann_cond(self, neumann_cond):
        """
        Función que aplica condiciones de contorno neumann, a ambos contornos del intervalo
        :param dirichlet_cond: tuple
        :return:
        """

        self.elementary_vector[0] -= neumann_cond[0] if neumann_cond[0] is not None else 0
        self.elementary_vector[-1] -= neumann_cond[1] if neumann_cond[1] is not None else 0

    def _apply_dirichlet_cond(self, dirichlet_cond):
        """
        Función que aplica condiciones de contorno dirichlet, a ambos contornos del intervalo
        :param dirichlet_cond: tuple
        :return:
        """
        if dirichlet_cond[0] is not None:
            self.global_matrix[0][0]  = G
            self.elementary_vector[0] = G*dirichlet_cond[0]

        if dirichlet_cond[1] is not None:
            self.global_matrix[-1][-1] = G
            self.elementary_vector[-1] = G*dirichlet_cond[1]

    def solver_mef(self, x: int) -> float:
        """
        Devuelve la solución de la ecuación diferencial en un punto,
        utiliza la interpolación de lagrange para calcular el valor
        :param x: float
        :return: float
        """
        result = 0
        points = self.mesh.get_points()
        # Utilizamos los valores de X obtenidos por el sistema de ecuaciones
        for i in range(len(self.solution)):
            fi = 1
            for j in range(len(points)):
                if i != j:
                    fi *= (x - points[j]) / (points[i] - points[j])
            result += self.solution[i] * fi
        return result