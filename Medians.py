def sortList(A):
    """Método que ordena una lista."""
    return A

def Median_Of_Median(A,i):
    """Método que busca la mediana de la lista."""
    sublistas = [A[j:j+5] for j in range(0,len(A),5)]
    medianas = [sortList(sublistas[i])[len(sublistas[i]/2)] for i in range(0,len(sublistas))]
    
    #-----------------Aquí se evalúa el caso base de las medianas---------------------------
    if (len(medianas) <= 5):
        pivot = sortList(medianas)[len(medianas)/2]
    else:
        pivot = Median_Of_Median(medianas,0)

    return pivot