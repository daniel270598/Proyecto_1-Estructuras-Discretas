import random, csv, timeit
import cProfile                                                     # Importo cProfile para realizar profilling.
import pstats                                                       # Lo importo ya que me permitira transformar la información del timing.
import random, csv, timeit                                          # Importa módulos externos.
import matplotlib.pyplot as plt                                     # Importa el módulo de matplotlib.
import numpy as np                                                  # Importa numpy.

class QuickSort:

    def __init__(self,Q=None):
        """ 
            Constructor del QuickSort
           *Atributo lista Q
        """
        
        self.Q = Q
    
    def setQ(self,Q):
        """
            Set del atributo Q
            *Modifica el atributo Q
        """
        self.Q = Q
    
    def quickSortRandom(self, Q, inicio, final):
        """
            QuickSort Random
            *Ordena los elementos de una lista creados aleatoriamente
        """
        if Q!= None:
            # Definimos el caso base del quicksort
            if final == 1 or final == 0:
                return Q
            
            if inicio < final:

                # Alteramos al final para que sea random porqué después será el pivote en ordenar 
                final_alter = random.randrange(inicio, final)
                self.swap(self.Q, final, final_alter)
        
                # Se obtiene la posición del pivote y se ordena según el pivote
                indice = self.ordenar(self.Q, inicio, final)
        
                self.quickSortRandom(self.Q, inicio, indice - 1)
                self.quickSortRandom(self.Q, indice + 1, final)
    
    def quickSort(self, Q, inicio, final):
        """
            QuickSort Normal
            *Ordena los elementos de una lista
        """
        if Q!= None:
            # Definimos el caso base del quicksort
            if  final == 1 or final == 0:
                return Q

            if inicio < final:
        
                # Se obtiene la posición del pivote y se ordena según el pivote
                indice = self.ordenar(self.Q, inicio, final)

                self.quickSort(self.Q, inicio, indice - 1)
                self.quickSort(self.Q, indice + 1, final)

    def ordenar(self, Q, inicio, final):
    
        pivot = final
        indice = inicio
        indice2 = inicio
    
        # Ordenamos los menores a la izquierda y los mayores a la derecha
        while indice2 < final:

            # Si hay menores que el pivote un indice los mueve de primeros 
            if self.Q[pivot] > self.Q[indice2]:
                self.swap(self.Q, indice, indice2)
                indice += 1
            indice2 +=1
    
        # Como el pivote es el ultimo lo movemos a donde está el indice
        # para ubicarlo en su posicion correcta en el arreglo
        self.swap(self.Q,indice,pivot)
        return indice


    def swap(self, Q, num1, num2):
        """
            Método swap
            *Intercambia dos elementos de la lista
        """
        # definimos un método para hacer el intercambio
        self.Q[num1], self.Q[num2] = self.Q[num2], self.Q[num1]
        
        
    def quickSort_timing(self, start, stop, step):
        """
            Metodo de timing para el quickSort
            *Imprime los tiempos de corrida del quickSort
        """
        # Método de timing para el quickSort
        global t 
        t = self
        results = []
        population = list(range(0, stop))
    
        for n in range(start, stop, step):

            size = start + n
            t.Q = random.sample(population, size)
            print("Size={}".format(size))
            tn = timeit.timeit("t.quickSort(t.Q, 0, len(t.Q)-1)", number=500, globals=globals())
            
            results.append((size, tn))
        return results
    
    def quickSort_time_save(self, filename="datos/quickSort.csv", start=5, stop=100, step=5):
        """
            Método guardar del quickSort
            *Guarda los tiempos de corrida del quickSort
        """
        # Método para guardar los resultados del timing
        results = self.quickSort_timing(start, stop, step)
    
        with open(filename, 'w', newline='') as csvfile:
        
            writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['i', 'n', 'time'])

            # Enumeramos las columnas
            for i, (n, tn) in enumerate(results):
                writer.writerow([i, n, tn])
            
    def quickSort_rand_timing(self, start, stop, step):
        """
            Metodo de timing para el quickSort
            *Imprime los tiempos de corrida del quickSort
        """
        # Método de timing para el quickSort Random
        global b 
        b = self
        results = []
        population = list(range(0, stop))
    
        for n in range(start, stop, step):

            size = start + n
            b.Q = random.sample(population, size)
            print("Size={}".format(size))
            tn = timeit.timeit("b.quickSortRandom(b.Q, 0, len(b.Q)-1)", number=500, globals=globals())
            
            results.append((size, tn))
        return results
    
    def quickSort_rand_time_save(self, filename="datos/quickSort_Random.csv", start=5, stop=100, step=5):
        """
            Método guardar del quickSort Random
            *Guarda los tiempos de corrida del quickSort
        """
        # Método para guardar los resultados del timing
        results = self.quickSort_rand_timing(start, stop, step)
    
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['i', 'n', 'time'])

            # Enumeramos las columnas
            for i, (n, tn) in enumerate(results):
                writer.writerow([i, n, tn])
                
        
    def graficar_quickSort(self):
        """
            Gráfica los tiempos del quickSort
        """
        # Método graficar el QuickSort:
  
        csvarchivo = open('datos/quickSort.csv')                
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
        """
            Gráfica los tiempos del quickSort
        """        
        # Método graficar el QuickSort Random:
  
        csvarchivo = open('datos/quickSort_Random.csv')                
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
        """
            Método del timing para el quickSort
            *Crea los tiempos de corrida para el quickSort
        """    
        if self.Q != None: 
            print("\n---- Caso específico: Q = {} ---- Posicion = 0\n".format(self.Q))
            cProfile.runctx('self.quickSort(self.Q, 0, len(self.Q)-1)', globals(),locals())
        print("\n---- Ahora casos varios con elementos aleatorios ----\n")
        self.quickSort_time_save()              # Llama para probar timing diferentes casos.
        self.graficar_quickSort()                  # Llama para mostrar una gráfica.
        self.Q.clear()                                     # Elimina los elementos en A.
        self.Q = None                                      # Le asigna a A None(NULL).
        print("\n Atención usuario, ha sido exportado el respectivo documento CSV con los resultados anteriores.")
        
    def timing_quickSort_Rand(self):
        """
            Método del timing para el quickSort
            *Crea los tiempos de corrida para el quickSort
        """   
        if self.Q != None: 
            print("\n---- Caso específico: Q = {} ---- Posicion = 0\n".format(self.Q))
            cProfile.runctx('self.quickSort(self.Q, 0, len(self.Q)-1)', globals(),locals())
        print("\n---- Ahora casos varios con elementos aleatorios ----\n")
        self.quickSort_rand_time_save()              # Llama para probar timing diferentes casos.
        self.graficar_quickSort_Rand()                  # Llama para mostrar una gráfica.
        self.Q.clear()                                     # Elimina los elementos en A.
        self.Q = None                                      # Le asigna a A None(NULL).
        print("\n Atención usuario, ha sido exportado el respectivo documento CSV con los resultados anteriores.")


