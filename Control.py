"""
    * Módulo principal aquí se localiza el método main.
    * Clase Control: 
"""

from Interfaz import Interfaz                                       # Importa la clase Interfaz.
from QuickSort import QuickSort                                     # Importa el Quicksort.
from Medians import Medianas                                        # Importa el módulo Medianas la clase Medianas.
import os                                                           # Importa para accesar al sistema.
import msvcrt                                                       # Importa.

# _________________________________________________________________ Define la clase Control
class Control:
    """
        * Clase la cual se encargará de llamar a los diferentes
        * métodos para así controlar el flujo del programa.
    """
    # ------------------------------------------------------------- Constructor
    #def __init__(self):
       # pass

    # ------------------------------------------------------------- Método el cual se encargará de llamar a los 
    # ------------------------------------------------------------- diferentes métodos para continuar el flujo
    # ------------------------------------------------------------- del programa.
    def secuencia(self):
        """
            * Método secuencia:
            * Método el cual se encarga de llamar a los 
            * diferentes métodos para continuar con el
            * flujo del programa.
        """
        opc = 0
        while (opc != 3):
            os.system('cls')                                        # Limpia pantalla.
            cInterfaz = Interfaz()                                  # Creo el objeto Interfaz.
            cInterfaz.menu_Principal()                              # Llamamos al método externo.
            opc = int(input("\nIngrese la opcion: "))               # Aquí almacenamos en opc lo que digite el usuario.
            # ______________________________________________________ Bloque condicional el cual evalúa lo que
            #                                                        ingreso el usuario.
            if opc == 1:                                            # Submenu Quicksort.
                self.control_menu_Quicksort()                       # Llama al método interno.
            elif opc == 2:                                          # Submenu Medianas.
                self.control_menu_Medians()                         # Llama al método interno.
            elif opc == 3:                                          # Salir.
                exit()                                              # Sale del programa.
            # ______________________________________________________ Fin del bloque.
        pass

    # -------------------------------------------------------------- Método que permite crea una lista
    def crearLista(self):
        a = []                                                      # Creamos una lista vacía.
        # __________________________________________________________ Ciclo para agregar elementos.
        while (len(a) == 0) or ((msvcrt.getch().decode()) != chr(27)):  # Guarda la tecla presionada por el usuario.
            os.system("cls")                                            # Limpia pantalla.
            print("--- Agregando Elementos a la Lista ---")             # Mensaje al usuario.
            print("\na = {}".format(a))
            # ------------------------------------------------------ Aquí almacenamos en la lista lo que digite el usuario.
            a.append(int(input("\nIngrese el elemento: ")))
            print("Presiones ESC para salir, otra tecla para continuar..")
        return a                                                    # Retornamos la lista.

    # -------------------------------------------------------------- Método el cual permite manejar el menu - quicksort.
    def control_menu_Quicksort(self):
        opc2 = 0                                                    # Inicializa opc2.
        cInterfaz = Interfaz()  
        qs = QuickSort()                                    # Creo el objeto Interfaz.
        #___________________________________________________________ Inicio del ciclo while - Iterar menú.
        while (opc2 != 7): # ///////////// Numero a poner el de la opcion SALIR ///////////////////////
            os.system('cls')                                            # Limpia pantalla
            cInterfaz.menu_Quicksort()                              # Llama método externo.
            opc2 = int(input("\nIngrese la opcion: "))              # Aquí almacenamos en opc2 lo que digite el usuario.
            #------------------------------------------------------- Bloque de evaluación para menu quicksort.
            if opc2 == 1:
                os.system("cls")
                a = self.crearLista()
                qs = QuickSort(a)
            elif opc2 == 2:
                os.system("cls")
                qs.quickSortRandom(a,0,len(a)-1)
                print(a)
                input("\nPresione TECLA para continuar...")                 
            elif opc2 == 3:
                os.system("cls")
                qs.quickSort(a,0,len(a)-1)
                print(a)
                input("\nPresione TECLA para continuar...")                
            elif opc2 == 4:
                os.system("cls")
                qs.timing_quickSort_Rand()
                input("\nPresione TECLA para continuar...")                 
            elif opc2 == 5:
                os.system("cls")
                qs.timing_quickSort()
                input("\nPresione TECLA para continuar...")                
            elif opc2 == 6:
                os.system("cls")
                qs.quickSort_rand_time_save()
                qs.quickSort_time_save()
                input("\nPresione TECLA para continuar...")                 

            #qs.quickSort()
            #------------------------------------------------------- Fin bloque de evaluación.
            #_______________________________________________________ Fin bloque while.
        pass

    # -------------------------------------------------------------- Método el cual permite manejar el menu - Medians.
    def control_menu_Medians(self):
        opc2 = 0                                                    # Inicializa opc2.
        cInterfaz = Interfaz()                                      # Creo el objeto Interfaz.
        ms = Medianas([5,6,4,8,3,12,2,9,1,15])                      # Crea ms de tipo Medianas.
        #___________________________________________________________ Inicio del ciclo while - Iterar menú.
        while (opc2 != 6):
            os.system('cls')                                        # Limpia pantalla.
            cInterfaz.menu_Median_of_Medians()                      # Llama método externo.
            opc2 = int(input("\nIngrese la opcion: "))              # Aquí almacenamos en opc2 lo que digite el usuario.
            #------------------------------------------------------- Bloque de evaluación para menu quicksort.
            if opc2 == 1:                                           # Opción crear Lista.
                a = self.crearLista()
                ms.set_A(a)                                         # Cambiamos la lista en el objeto ms (Medianas).
            elif opc2 == 2:                                         # Opción Probar Medianas.
                os.system("cls")
                print("---- Calculando Mediana ----")
                print("\n Lista actual = {}\t Cantidad = {}".format(ms.A,len(ms.A)))
                indice = int(input("\n Indice a buscar (0-{}): ".format(len(ms.A))))
                print("\n Resultado de la Mediana = {}".format(ms.median_of_medians(ms.A,indice)))
                input("\nPresione TECLA para continuar...")         # Solo para visualizar resultado.
            elif opc2 == 3:                                         # Opción Probar Sort5.
                os.system("cls")
                print("---- Calculando Mediana ----")
                print("\n Lista actual = {}\t Cantidad = {}".format(ms.A,len(ms.A)))
                print("\n Lista Ordenada: {}".format(ms.sort(ms.A)))
                input("\nPresione TECLA para continuar...")         # Solo para visualizar resultado.
            elif opc2 == 4:                                         # Opción Timing Medianas.
                os.system("cls")
                ms.timing_Median_of_Medians()                       # Llama un método externo.
                input("\nPresione TECLA para continuar...")         # Solo para visualizar resultado.
            elif opc2 == 5:                                         # Opción Timing Sort5.
                os.system("cls")
                ms.timing_Sort_5()                                  # Llama un método externo.
                input("\nPresione TECLA para continuar...")         # Solo para visualizar resultado.
            #------------------------------------------------------- Fin bloque de evaluación.
        #___________________________________________________________ Fin bloque while.
        pass

# ------------------------------------------------------------------ Bloque Principal - Main
if __name__ == "__main__":
    contr = Control()
    contr.secuencia()
    pass