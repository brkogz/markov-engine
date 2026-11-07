import numpy as np

def validate_stochastic_matrix(P: np.ndarray, tol: float = 1e-8) -> None:
    """
    Validate that P is a stochastic matrix (Hoel-Port-Stone 1.2, Eq. 6-8).
    :param P: stochastic matrix
    :param tol: tolerance parameter
    :raises ValueError: If P is not a 2D square matrix, has negative entries, or rows do not sum to 1.
    """
    if P.ndim != 2:
        raise ValueError("P must be a 2-dimensional array.")
    elif P.shape[0] != P.shape[1]:
        raise ValueError("P must be a square matrix.")
    elif not np.all(P >= -tol):
        raise ValueError("P elements must be non-negative.")
    row_sums = np.sum(P, axis=1)
    if not np.allclose(row_sums, 1, atol=tol):
        raise ValueError("Row sums of transition matrix must equal 1.0.")






