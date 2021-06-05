from Domain.Mesh import Mesh
from Controller.SolverMef1D import SolverMef1D
from View.SolutionView import SolutionView
import numpy as np

# Números de elementos
elements = 3
# Función del lado derecho de la ecuación de poisson
function = lambda x: 1 - pow(x,2)
# Solución para comprobar el resultado, se puede poner a None si se desconoce
solution = lambda x: (pow(x,4)/12) - (pow(x,2)/2) + x - 7/12
#Condiciones de contorno
n_cond = [1, None]
d_cond = [None, 0]
#Intervalo
interval = [0, 1]

if __name__ == '__main__':
    m    = Mesh(elements, a=interval[0], b=interval[1])
    m_g  = SolverMef1D(m, function, neumann_cond=n_cond, dirichlet_cond=d_cond)
    view = SolutionView(40,a=interval[0], b=interval[1])
    view.view(m_g, solution=solution)

