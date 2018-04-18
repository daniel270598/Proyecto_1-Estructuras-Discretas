def sort5(A):
    """Método que ordena una lista."""
    for i in range(1, len(A)):
        b = A[i]
        j = i -1
        while j >= 0 and b < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = b   
    return A