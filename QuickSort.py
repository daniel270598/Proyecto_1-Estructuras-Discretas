import random


"""------------------------------------- QuickSort con pivote Random --------------------------------"""

def quickSortRandom(a, inicio, final):
    
    # Definimos el caso base del quicksort
    if final == 1 or final == 0:

        return a


    if inicio < final:
        
        # Alteramos al final para que sea random porqué después será el pivote en ordenar 
        final_alter = random.randrange(inicio, final)
        swap(a, final, final_alter)
        
        # Se obtiene la posición del pivote y se ordena según el pivote
        indice = ordenar(a, inicio, final)
        
        quickSort(a, inicio, indice - 1)
        quickSort(a, indice + 1, final)
        

"""------------------------------------- QuickSort con pivote Definido --------------------------------"""


def quickSort(a, inicio, final):
    # Definimos el caso base del quicksort
    if  final == 1 or final == 0:

        return a

    if inicio < final:
        
        # Se obtiene la posición del pivote y se ordena según el pivote
        indice = ordenar(a, inicio, final)

        quickSort(a, inicio, indice - 1)
        quickSort(a, indice + 1, final)

def ordenar(b, inicio, final):
    
    pivot = final
    indice = inicio
    indice2 = inicio
    
    # Ordenamos los menores a la izquierda y los mayores a la derecha
    while indice2 < final:

        # Si hay menores que el pivote un indice los mueve de primeros 
        if b[pivot] > b[indice2]:
            swap(b, indice, indice2)
            indice += 1
        indice2 +=1
    
    # Como el pivote es el ultimo lo movemos a donde está el indice
    # para ubicarlo en su posicion correcta en el arreglo
    swap(b,indice,pivot)
    return indice


def swap(c, num1, num2):
    
    # definimos un método para hacer el intercambio
    c[num1], c[num2] = c[num2], c[num1]