class Node:
    def __init__(self, id: int, element: int, shape_function):
        self.id = id
        self.shape_function = shape_function
        self.element = element

    def __str__(self) -> str:
        return "id: %i - element: %i - shape function: %i\n" % (self.id, self.element, self.shape_function(0))

    def __repr__(self) -> str:
        return self.__str__()



