
# Shape functions
shape_function_derivative = [
    lambda chi: 3*(2*chi - 1),
    lambda chi: -12*chi,
    lambda chi: 3*(2*chi + 1),
]

shape_function = [
    lambda chi: 1/2*chi*(chi - 1),
    lambda chi: 1 - pow(chi, 2),
    lambda chi: 1/2*chi*(chi + 1),
]

#Gauss integration data
gauss_points = [-0.57735, 0.57735] #[0, -0.538469, 0.538469, -0.90618, 0.90618]
weigths = [1,1] #[0.568889, 0.568889, 0.478629, 0.478629, 0.236927, 0.236927]