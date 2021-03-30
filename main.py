from Controller.SolverMef1D import SolverMef1D
from Domain.Mesh import Mesh
from Domain.GlobalMatrix import GlobalMatrix
from Utils import shape_functions

if __name__ == '__main__':
    m = Mesh(3)
    print(m.nodes)
    #m_g = GlobalMatrix(m, lambda x: x - 1)
    #print(m_g.solver_system_equations())

