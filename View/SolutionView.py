import matplotlib.pyplot as plt
from Controller.SolverMef1D import SolverMef1D
import numpy as np

class SolutionView:
    """n: int, a: int = 0, b: int = 1"""
    def __init__(self, n: int, a: int = 0, b: int = 1):
        self.X = np.arange(a, b, (b-a)/n)
        self.X = np.append(self.X, b)

    def view(self, solver: SolverMef1D, solution = None):
        y = [solver.solver_mef(x) for x in self.X]
        plt.plot(self.X, y)
        if solution:
            plt.plot(self.X, [solution(x) for x in self.X])
        plt.title("FEM Solution")
        plt.ylabel('U(x)')
        plt.xlabel('x')
        plt.show()