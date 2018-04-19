from sort import sort5                                              # Importo sort5 del módulo sort.
import cProfile                                                     # Importo cProfile para realizar profilling.
import pstats                                                       # Lo importo ya que me permitira transformar la información del timing.
import csv

# __________________________________________________________________ Clase Medianas.
class Medianas:

    def __init__(self,A):
        self.A = A

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

    def timing_Median_of_Medians(self):
        """
            * Método timing_Median_of_Medians:
            * Se encarga de dar los tiempos del método de median_of_medians() 
            * con sus diferentes operaciones de forma detallada.
        """
        cProfile.runctx('self.median_of_medians(self.A, len(self.A)//2)', globals(),locals(),'medians.csv')
        p = pstats.Stats('medians.csv')
        p.sort_stats('cumulative').print_stats(10)
        # Se le manda el método como una hilera, se le manda las variables globales y las locales
        # así para que los encuentre. Por ejemplo antes no encontraba el objeto self.

    def graficar_Median_of_Medians(self):
        """
            * Método graficar_Median_of_Medians:
            * Se encarga de graficar lo que sería el método de median_of_medians().
        """

    def exportar_Median_of_Medians_CSV(self, filename="Cuadernos/medians.csv", start=10, stop=100, step=5):
        """
            * Método exportar_Median_of_Medians_CSV:
            * Método el cual exporta un archivo CSV con diferentes casos.
        
        results = timing_bubble(start, stop, step)
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['i', 'n', 'time(n)'])
            for i, (n, tn) in enumerate(results):
                writer.writerow([i, n, tn])
        """