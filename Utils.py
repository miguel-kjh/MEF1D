
# Funciones de forma cuadradas
shape_function_derivative = [
    lambda chi: (2*chi - 1)/2,
    lambda chi: -2*chi,
    lambda chi: (2*chi + 1)/2,
]

shape_function = [
    lambda chi: 1/2*chi*(chi - 1),
    lambda chi: 1 - pow(chi, 2),
    lambda chi: 1/2*chi*(chi + 1),
]

#Datos necesarios para la integración con el método de Gausse
gauss_points = [-0.57735, 0.57735]
weigths = [1,1]

#Número grande para las condiciones de Dirichlet
G = 10e8