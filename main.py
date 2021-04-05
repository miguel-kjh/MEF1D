from Domain.Mesh import Mesh
from Controller.SolverMef1D import SolverMef1D
from View.SolutionView import SolutionView

elements = 3
function = lambda x: 1 - pow(x,2)
n_cond = [1, None]
d_cond = [None, 0]
interval = [0, 1]

if __name__ == '__main__':
    m    = Mesh(elements, a=interval[0], b=interval[1])
    m_g  = SolverMef1D(m, function, neumann_cond=n_cond, dirichlet_cond=d_cond)
    view = SolutionView(a=interval[0], b=interval[1])
    view.view(m_g)

