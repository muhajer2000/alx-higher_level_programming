#!/usr/bin/python3
"""" module import for matrix divied method """


def matrix_divided(matrix, div):
    """" function divided matrix

    Args:
        matrix : row of intger to divied
        div: number will add to matrix


    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    
    Returns:
        list: List of lists representing divided matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
         raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for ind in matrix:
        if not isinstance(ind, list) or len(ind) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(ind) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in ind:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
