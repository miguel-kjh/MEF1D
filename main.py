from Domain.Mesh import Mesh
from Controller.SolverMef1D import SolverMef1D
from View.SolutionView import SolutionView
import numpy as np

elements = 3
#k = 205
function = lambda x: 1 - pow(x,2) #np.sin(np.pi*x) #1 - pow(x,2) #np.exp(-k*(x-5)**2)
solution = None#lambda x: np.sin(np.pi*x)/np.pi**2
n_cond = [1, None]
d_cond = [None, 0] #[0, 0]
interval = [0, 1] #[0, 10]

if __name__ == '__main__':
    m    = Mesh(elements, a=interval[0], b=interval[1])
    m_g  = SolverMef1D(m, function, neumann_cond=n_cond, dirichlet_cond=d_cond)
    view = SolutionView(40,a=interval[0], b=interval[1])
    view.view(m_g, solution=solution)

