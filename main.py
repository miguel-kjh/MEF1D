from Domain.Mesh import Mesh
from Controller.SolverMef1D import SolverMef1D

elements = 3
function = lambda x: 1 - pow(x,2)
n_cond = [1, None]
d_cond = [None, 0]

if __name__ == '__main__':
    m = Mesh(elements)
    m_g = SolverMef1D(m, function, neumann_cond=n_cond, dirichlet_cond=d_cond)
    print(m_g.solver_mef())

