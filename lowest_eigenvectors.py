def lowest_eigenvectors(square_matrix):
    from numpy import linalg, linspace, sqrt, sin, pi, sum, sort, argsort

    M_rows = len(square_matrix)
    count = 0
    while count < M_rows:
        M_columns = len(square_matrix[count])
        if not M_rows == M_columns:
            return print("Square matrix needs to have M rows and M columns, M >= 1.")

    (V, D) = linalg.eig(square_matrix)
    ordered_indices = argsort(V)
    eigenvalues = (V[ordered_indices[0:number_of_eigenvectors]])
    eigenvectors = (D[ordered_indices[0:number_of_eigenvectors]])
    return eigenvalues, eigenvectors