from Domain.Mesh import Mesh
from Controller.SolverMef1D import SolverMef1D
from Utils import shape_functions

if __name__ == '__main__':
    m = Mesh(3)
    print(m.nodes)
    print(m.get_nodes_of_element(2))
    m_g = SolverMef1D(m, lambda x: x - 1)
    print(m_g.solver_mef())

