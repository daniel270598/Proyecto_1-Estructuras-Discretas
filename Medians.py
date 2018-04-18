import sort

def median_of_medians(A,i):
    """Método que busca la mediana de la lista."""
   sublistas = [A[j:j+5] for j in range(0,len(A),5)]
   medianas = [sort.sortList(sublista)[len(sublista)//2] for sublista in sublistas]
    
    #-----------------Aquí se evalúa el caso base de las medianas---------------------------
    if (len(medianas) <= 5):
        pivot = sort.sortList(medianas)[len(medianas)//2]
    else:
        pivot = median_of_medians(medianas,len(medianas)//2)

    #------------ Se realiza la particion del pivot para obtener la mediana de las medianas-------------
    l = [j for j in A if j < pivot]
    h = [j for j in A if j > pivot]

    k = len(l)
    if i < k:
        return median_of_medians(l,i)
    elif i > k:
        return median_of_medians(h,i-k-1)
    else: #pivot = k
        return pivot