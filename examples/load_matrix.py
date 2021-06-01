import pandas as pd

def load_matrix(path_to_matrix):
    """ Load a score matrix.
    
        Args:
          path_to_matrix: path to the `*.data` file.
    """
    matrix = pd.read_csv(path_to_matrix, sep=' ', header=None)
    return matrix
