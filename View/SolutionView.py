import matplotlib.pyplot as plt
from Controller.SolverMef1D import SolverMef1D
import numpy as np

class SolutionView:
    def __init__(self, a:int = 0, b: int = 1):
        n = 10
        self.X = np.arange(a, b, (b-a)/n)
        self.X = np.append(self.X, b)

    def view(self, solver: SolverMef1D):
        y = [solver.solver_mef(x) for x in self.X]
        plt.plot(self.X, y)
        plt.show()