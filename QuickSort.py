import random


class QuickSort:

    def __init__(self,Q=None):
        self.Q = Q
    
    def quickSortRandom(self, Q, inicio, final):
        # Definimos el caso base del quicksort
        if final == 1 or final == 0:
            return Q
        if inicio < final:

            # Alteramos al final para que sea random porqué después será el pivote en ordenar 
            final_alter = random.randrange(inicio, final)
            self.swap(Q, final, final_alter)
        
            # Se obtiene la posición del pivote y se ordena según el pivote
            indice = self.ordenar(Q, inicio, final)
        
            self.quickSortRandom(Q, inicio, indice - 1)
            self.quickSortRandom(Q, indice + 1, final)
    
    def quickSort(self, Q, inicio, final):
        # Definimos el caso base del quicksort
        if  final == 1 or final == 0:
            return Q

        if inicio < final:
        
            # Se obtiene la posición del pivote y se ordena según el pivote
            indice = self.ordenar(Q, inicio, final)

            self.quickSort(Q, inicio, indice - 1)
            self.quickSort(Q, indice + 1, final)

    def ordenar(self, Q, inicio, final):
    
        pivot = final
        indice = inicio
        indice2 = inicio
    
        # Ordenamos los menores a la izquierda y los mayores a la derecha
        while indice2 < final:

            # Si hay menores que el pivote un indice los mueve de primeros 
            if Q[pivot] > Q[indice2]:
                self.swap(Q, indice, indice2)
                indice += 1
            indice2 +=1
    
        # Como el pivote es el ultimo lo movemos a donde está el indice
        # para ubicarlo en su posicion correcta en el arreglo
        self.swap(Q,indice,pivot)
        return indice


    def swap(self, Q, num1, num2):
    
        # definimos un método para hacer el intercambio
        Q[num1], Q[num2] = Q[num2], Q[num1]

