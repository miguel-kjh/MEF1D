class Node:
    def __init__(self, id: int, element, shape_function, shape_function_derivative, interval: tuple):
        self.id = id
        self.shape_function_derivative = shape_function_derivative
        self.shape_function = shape_function
        self.element = element
        self.interval = interval

    def __str__(self) -> str:
        return "id: %i - element: %s - interval %s -shape function: %i\n" % (self.id, self.element,self.interval, self.shape_function(1))

    def __repr__(self) -> str:
        return self.__str__()



