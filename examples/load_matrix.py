import pandas as pd

path_to_matrix = 'example.data'
matrix = pd.read_csv(path_to_matrix, sep=' ', header=None)
print(matrix)
