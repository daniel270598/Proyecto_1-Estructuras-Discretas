import random, csv, timeit
import cProfile                                                     # Importo cProfile para realizar profilling.
import pstats                                                       # Lo importo ya que me permitira transformar la información del timing.
import random, csv, timeit                                          # Importa módulos externos.
import matplotlib.pyplot as plt                                     # Importa el módulo de matplotlib.
import numpy as np                                                  # Importa numpy.

class QuickSort:

    def __init__(self,Q=None):
        self.Q = Q
    
    def quickSortRandom(self, Q, inicio, final):
        if Q!= None:
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
        if Q!= None:
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
        
        
    def quickSort_timing(self, start, stop, step):
        # Método de timing para el quickSort
        global a
        a = self
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
        
        # Método para guardar los resultados del timing
        results = self.quickSort_timing(start, stop, step)
    
        with open(filename, 'w', newline='') as csvfile:
        
            writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['i', 'n', 'time'])

            # Enumeramos las columnas
            for i, (n, tn) in enumerate(results):
                writer.writerow([i, n, tn])
            
    def quickSort_rand_timing(self, start, stop, step):

        # Método de timing para el quickSort Random
        global b 
        b = self
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
        
        # Método para guardar los resultados del timing
        results = self.quickSort_rand_timing(start, stop, step)
    
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['i', 'n', 'time'])

            # Enumeramos las columnas
            for i, (n, tn) in enumerate(results):
                writer.writerow([i, n, tn])
                
        
    def graficar_quickSort(self):
        
        # Método graficar el QuickSort:
  
        csvarchivo = open('Cuadernos/quickSort.csv')                
        cont = 0                                                    
        
        if csvarchivo:
            entrada = csv.reader(csvarchivo)                        
            ns = []                                                 
            tiempos = []

            # Avanzo en entrada.   
            for reg in entrada:
                if cont == 0:
                    cont = 1
                else:
                    linea = reg[0]                                 
                    _tupla1 = linea.partition(';')
                    _tupla2 = _tupla1[2].partition(';')
                    n = _tupla2[0]
                    tiempo = _tupla2[2]
                    cont = cont+1
                    ns.append(int(n))                               
                    tiempos.append(float(tiempo))                   
            plt.plot(ns,tiempos, label = "time(n)")
            plt.title("Gráfica QuickSort")
            plt.show()
        csvarchivo.close()
    

    def graficar_quickSort_Rand(self):
        
        # Método graficar el QuickSort Random:
  
        csvarchivo = open('Cuadernos/quickSort_Rand.csv')                
        cont = 0                                                    
        
        if csvarchivo:
            entrada = csv.reader(csvarchivo)                        
            ns = []                                                 
            tiempos = []

            # Avanzo en entrada.   
            for reg in entrada:
                if cont == 0:
                    cont = 1
                else:
                    linea = reg[0]                                 
                    _tupla1 = linea.partition(';')
                    _tupla2 = _tupla1[2].partition(';')
                    n = _tupla2[0]
                    tiempo = _tupla2[2]
                    cont = cont+1
                    ns.append(int(n))                               
                    tiempos.append(float(tiempo))                   
            plt.plot(ns,tiempos, label = "time(n)")
            plt.title("Gráfica QuickSort")
            plt.show()
        csvarchivo.close()

        
    def timing_quickSort(self):
 
        if self.Q != None: 
            print("\n---- Caso específico: Q = {} ---- Posicion = 0\n".format(self.Q))
            cProfile.runctx('self.quickSort(self.Q, 0)', globals(),locals())
        print("\n---- Ahora casos varios con elementos aleatorios ----\n")
        self.quickSort_time_save()              # Llama para probar timing diferentes casos.
        self.graficar_quickSort()                  # Llama para mostrar una gráfica.
        self.Q.clear()                                     # Elimina los elementos en A.
        self.Q = None                                      # Le asigna a A None(NULL).
        print("\n Atención usuario, ha sido exportado el respectivo documento CSV con los resultados anteriores.")
        
    def timing_quickSort_Rand(self):
 
        if self.Q != None: 
            print("\n---- Caso específico: Q = {} ---- Posicion = 0\n".format(self.Q))
            cProfile.runctx('self.quickSort(self.Q, 0)', globals(),locals())
        print("\n---- Ahora casos varios con elementos aleatorios ----\n")
        self.quickSort_rand_time_save()              # Llama para probar timing diferentes casos.
        self.graficar_quickSort_Rand()                  # Llama para mostrar una gráfica.
        self.Q.clear()                                     # Elimina los elementos en A.
        self.Q = None                                      # Le asigna a A None(NULL).
        print("\n Atención usuario, ha sido exportado el respectivo documento CSV con los resultados anteriores.")


