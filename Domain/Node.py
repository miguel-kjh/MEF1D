class Node:
    """
    Clase Node, almacena la información necesaria de cada nodo de la malla 1D.
    """
    def __init__(self, id: int, element: int, shape_function, shape_function_derivative, interval: tuple):
        # Identificador del nodo
        self.id = id

        # Funciones de forma
        self.shape_function_derivative = shape_function_derivative
        self.shape_function = shape_function

        # El elemento al que pertenecen
        self.element = element

        # Su intervalo
        self.interval = interval

    def __str__(self) -> str:
        return "id: %i - element: %s - interval %s -shape function: %i\n" % (self.id, self.element,self.interval, self.shape_function(1))

    def __repr__(self) -> str:
        return self.__str__()



