from sort import sort5                                              # Importo sort5 del módulo sort.
from timing_sort import timing_sort,sort_time_save                  # Importa el timing sort.
import cProfile                                                     # Importo cProfile para realizar profilling.
import pstats                                                       # Lo importo ya que me permitira transformar la información del timing.
import random, csv, timeit                                          # Importa módulos externos.
import matplotlib.pyplot as plt                                     # Importa el módulo de matplotlib.
import numpy as np                                                  # Importa numpy.

# __________________________________________________________________ Clase Medianas.
class Medianas:
    # -------------------------------------------------------------- Constructor.
    def __init__(self,A=None):
        self.A = A
    
    # -------------------------------------------------------------- Método que permite modificar el atributo.
    def set_A(self,A):
        self.A.clear()
        self.A = A                                                  # Asigna al atributo el parámetro.

    # -------------------------------------------------------------- Método que saca la mediana de las medianas.
    def median_of_medians(self,A,i):
        """Método que busca la mediana de la lista."""
        sublistas = [A[j:j+5] for j in range(0,len(A),5)]
        medianas = [sort5(sublista)[len(sublista)//2] for sublista in sublistas]
        
        #-----------------Aquí se evalúa el caso base de las medianas---------------------------
        if (len(medianas) <= 5):
            pivot = sort5(medianas)[len(medianas)//2]
        else:
            pivot = self.median_of_medians(medianas,len(medianas)//2)

        #------------ Se realiza la particion del pivot para obtener la mediana de las medianas-------------
        l = [j for j in A if j < pivot]
        h = [j for j in A if j > pivot]

        k = len(l)
        if i < k:
            return self.median_of_medians(l,i)
        elif i > k:
            return self.median_of_medians(h,i-k-1)
        else: #pivot = k
            return pivot

    # -------------------------------------------------------------- Método el cual llama a los demas metodos para realizar timing.
    def timing_Median_of_Medians(self):
        """
            * Método timing_Median_of_Medians:
            * Se encarga de dar los tiempos del método de median_of_medians() 
            * con sus diferentes operaciones de forma detallada.
        """
        if self.A != None: 
            print("\n---- Caso específico: A = {} ---- Posicion = 0\n".format(self.A))
            cProfile.runctx('self.median_of_medians(self.A, 0)', globals(),locals())
            # Se le manda el método como una hilera, se le manda las variables globales y las locales
            # así para que los encuentre. Por ejemplo antes no encontraba el objeto self.
        #p = pstats.Stats('medians.csv') ------Esto es solo si guardo el resultado del profiling
        #p.sort_stats('cumulative').print_stats(10) -------Esto imprime el resultado del profiling.
        print("\n---- Ahora casos varios con elementos aleatorios ----\n")
        self.exportar_Median_of_Medians_CSV()                       # Llama para probar timing diferentes casos.
        self.graficar_Median_of_Medians()                           # Llama para mostrar una gráfica.
        print("\n Atención usuario, ha sido exportado el respectivo documento CSV con los resultados anteriores.")
        self.A.clear()
        self.A = None
        pass

    # -------------------------------------------------------------- Método el cual llama a los demas metodos para realizar timing.
    def timing_Sort_5(self): # Este método solo se encarga de invocar los métodos necesarios para el timing de sort5.
        """
            * Método timing_Median_of_Medians:
            * Se encarga de dar los tiempos del método de median_of_medians() 
            * con sus diferentes operaciones de forma detallada. 
            * Este llama los métodos necesarios para los resultados del timing sort5.
        """
        if self.A != None: 
            print("\n---- Caso específico: A = {} ----\n".format(self.A))
            cProfile.runctx('self.sort(self.A)', globals(),locals())
            # Se le manda el método como una hilera, se le manda las variables globales y las locales
            # así para que los encuentre. Por ejemplo antes no encontraba el objeto self.
        #p = pstats.Stats('sort5.csv') ------Esto es solo si guardo el resultado del profiling
        #p.sort_stats('cumulative').print_stats(10) -------Esto imprime el resultado del profiling.
        print("\n---- Ahora casos varios con elementos aleatorios ----\n")
        self.export_Sort5_CSV()                                     # Llama para probar timing diferentes casos.
        self.graficar_Sort5()                                       # Llama para mostrar una gráfica.
        print("\n Atención usuario, ha sido exportado el respectivo documento CSV con los resultados anteriores.")
        pass

    # -------------------------------------------------------------- Método el cual cálcula los tiempos en diferentes casos.
    def timing_medians(self,start, stop, step):
        """
            * Método que se encargá de evaluar el tiempo en diferentes casos de medians.
        """
        global _o
        _o = self
        results = []
        population = list(range(0, stop))
        for n in range(start, stop, step):
            size = start + n
            _o.A = random.sample(population, size)
            tn = timeit.timeit("_o.median_of_medians(_o.A,0)", number=500, globals=globals())
            print("\tn={}\tSize = {}\tTiempo={}".format(n,size,tn))
            results.append((size, tn))
        return results

    # --------------------------------------------------------------Método permite exportar un CSV.
    def exportar_Median_of_Medians_CSV(self,filename="datos/medians.csv", start=5, stop=100, step=5):
        """
            * Método exportar_Median_of_Medians_CSV:
            * Método el cual exporta un archivo CSV con diferentes casos.
        """
        results = self.timing_medians(start, stop, step)
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['i', 'n', 'time'])
            for i, (n, tn) in enumerate(results):
                writer.writerow([i, n, tn])

    # -------------------------------------------------------------- Método el cual permite ordenar una lista.
    def sort(self,a):
        """Método que permite accesar a sort5 a externos."""
        return sort5(a)

    # -------------------------------------------------------------- Método el cual hace timing del sort5.
    def timing_Sort5(self):
        """ Método para medir los tiempos de sort5. """
        timing_sort(10,1000,100)

    # -------------------------------------------------------------- Método el cual exporta el resultado del timing de sort5.
    def export_Sort5_CSV(self):
        """ Método para exportar en CSV los resultados del timing de sort5. """
        sort_time_save()

    # -------------------------------------------------------------- Método el cual muestra una gráfica de medianas.
    def graficar_Median_of_Medians(self):
        """
            * Método graficar_Median_of_Medians:
            * Se encarga de graficar lo que sería el método de median_of_medians().
        """
        csvarchivo = open('datos/medians.csv')                      # Abre el archivo.
        cont = 0                                                    # Defino cont
        if csvarchivo:
            entrada = csv.reader(csvarchivo)                        # Leer todos los registros.
            ns = []                                                 # Creando ns.
            tiempos = []                                            # Creando tiempos.
            # ----------------------------------------------------- Avanzo en entrada.   
            for reg in entrada:
                if cont == 0:
                    cont = 1
                else:
                    linea = reg[0]                                  # Leer los campos.
                    _tupla1 = linea.partition(';')
                    _tupla2 = _tupla1[2].partition(';')
                    n = _tupla2[0]
                    tiempo = _tupla2[2]
                    cont = cont+1
                    ns.append(int(n))                               # Agregar a lo último.
                    tiempos.append(float(tiempo))                   # Agregar a lo último.
            plt.plot(ns,tiempos, label = "time(n)")
            plt.title("Gráfica Medianas")
            plt.show()
        csvarchivo.close()
    
    # -------------------------------------------------------------- Método el cual muestra una gráfica de sort5.
    def graficar_Sort5(self):
        """
            * Método crear_Grafica_Sort5:
            * Método el cual produce una gráfica para mostrar sort5.
        """
        csvarchivo = open('datos/sort5.csv')                        # Abre el archivo.
        cont = 0                                                    # Defino cont
        if csvarchivo:
            entrada = csv.reader(csvarchivo)                        # Leer todos los registros.
            ns = []                                                 # Creando ns.
            tiempos = []                                            # Creando tiempos.
            # ----------------------------------------------------- Avanzo en entrada.   
            for reg in entrada:
                if cont == 0:
                    cont = 1
                else:
                    linea = reg[0]                                  # Leer los campos.
                    _tupla1 = linea.partition(';')
                    _tupla2 = _tupla1[2].partition(';')
                    n = _tupla2[0]
                    tiempo = _tupla2[2]
                    cont = cont+1
                    ns.append(int(n))                               # Agregar a lo último.
                    tiempos.append(float(tiempo))                   # Agregar a lo último.
            plt.plot(ns,tiempos, label = "time(n)")
            plt.title("Gráfica Sort5")
            plt.show()
        csvarchivo.close()