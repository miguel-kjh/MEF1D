from Domain.Mesh import Mesh
from Controller.SolverMef1D import SolverMef1D

elements = 3
function = lambda x: 1 - pow(x,2)

if __name__ == '__main__':
    m = Mesh(elements)
    m_g = SolverMef1D(m, function)
    print(m_g.solver_mef())

