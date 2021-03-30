from Controller.SolverMef1D import SolverMef1D
from Domain.Mesh import Mesh
from Utils import shape_functions

if __name__ == '__main__':
    m = Mesh(3)
    print(m.nodes)
