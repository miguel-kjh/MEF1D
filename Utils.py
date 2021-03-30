
# Shape functions derivates
shape_functions = [
    lambda chi: 3*(2*chi - 1),
    lambda chi: -12*chi,
    lambda chi: 3*(2*chi + 1),
]

#Gauss integration data
gauss_points = [-0.57735, 0.57735]
weigths = [1, 1]