import random, csv, timeit
from timing_quickSorts import quickSort_rand_time_save, quickSort_time_save

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
        
a = self

def quickSort_timing(self, start, stop, step):
    global a
    results = []
    population = list(range(0, stop))
    for n in range(start, stop, step):
        size = start + n
        a = random.sample(population, size)
        print("Size={}".format(size))
        tn = timeit.timeit("QuickSort.quickSort(a, 0, len(a)-1)", number=500, globals=globals())
        results.append((size, tn))
    return results

def quickSort_time_save(self, filename="quickSort.csv", start=10, stop=1000, step=100):
    results = quickSort_timing(start, stop, step)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['i', 'n', 'time'])
        for i, (n, tn) in enumerate(results):
            writer.writerow([i, n, tn])




def quickSort_rand_timing(self, start, stop, step):
    global b
    results = []
    population = list(range(0, stop))
    for n in range(start, stop, step):
        size = start + n
        b = random.sample(population, size)
        print("Size={}".format(size))
        tn = timeit.timeit("QuickSort.quickSortRandom(b, 0, len(b)-1)", number=500, globals=globals())
        results.append((size, tn))
    return results

def quickSort_rand_time_save(self, filename="quickSort_Random.csv", start=5, stop=100, step=5):
    results = self.quickSort_rand_timing(start, stop, step)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(cs vfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['i', 'n', 'time'])
        for i, (n, tn) in enumerate(results):
            writer.writerow([i, n, tn])
