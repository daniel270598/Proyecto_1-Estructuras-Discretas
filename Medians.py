from sort import sort5

def median_of_medians(A,i):
    """Método que busca la mediana de la lista."""
<<<<<<< HEAD
   sublistas = [A[j:j+5] for j in range(0,len(A),5)]
   medianas = [sort.sort5(sublista)[len(sublista)//2] for sublista in sublistas]
    
    #-----------------Aquí se evalúa el caso base de las medianas---------------------------
    if (len(medianas) <= 5):
        pivot = sort.sort5(medianas)[len(medianas)//2]
    else:
        pivot = median_of_medians(medianas,len(medianas)//2)
=======
    sublistas = [A[j:j+5] for j in range(0,len(A),5)]
    medianas = [sort5(sublistas[i])[len(sublistas//2)] for i in range(0,len(sublistas))]
    
    #-----------------Aquí se evalúa el caso base de las medianas---------------------------
    if (len(medianas) <= 5):
        pivot = sort5(medianas)[len(medianas)//2]
    else:
        pivot = median_of_medians(medianas,0)
>>>>>>> 3e94aa814a39643a6d2d4adf4377ae7b58ffb308

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