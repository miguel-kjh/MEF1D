
# Shape functions derivates
shape_functions = [
    lambda chi: 3*(2*chi - 1),
    lambda chi: -12*chi,
    lambda chi: 3*(2*chi + 1),
]

#Gauss integration data
gauss_points = [0, -0.538469, 0.538469, -0.90618, 0.90618]
weigths = [0.568889, 0.568889, 0.478629, 0.478629, 0.236927, 0.236927]