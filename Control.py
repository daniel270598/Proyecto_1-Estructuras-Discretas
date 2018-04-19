"""
    * Módulo principal aquí se localiza el método main.
    * Clase Control: 
"""

from Interfaz import Interfaz                                       # Importa la clase Interfaz.
import QuickSort as qs                                              # Importa el Quicksort.
import Medians as ms                                                # Importa el módulo Medianas.
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
        cInterfaz = Interfaz()                                      # Creo el objeto Interfaz.
        #___________________________________________________________ Inicio del ciclo while - Iterar menú.
        while (opc2 != 4): # ///////////// Numero a poner el de la opcion SALIR ///////////////////////
            os.system('cls')                                            # Limpia pantalla
            cInterfaz.menu_Quicksort()                              # Llama método externo.
            opc2 = int(input("\nIngrese la opcion: "))              # Aquí almacenamos en opc2 lo que digite el usuario.
            #------------------------------------------------------- Bloque de evaluación para menu quicksort.
            if opc2 == 1:
                os.system("cls")                                    # Limpia pantalla
            #qs.quickSort()
            #------------------------------------------------------- Fin bloque de evaluación.
            #_______________________________________________________ Fin bloque while.
        pass

    # -------------------------------------------------------------- Método el cual permite manejar el menu - Medians.
    def control_menu_Medians(self):
        opc2 = 0                                                    # Inicializa opc2.
        cInterfaz = Interfaz()                                      # Creo el objeto Interfaz.
        #___________________________________________________________ Inicio del ciclo while - Iterar menú.
        while (opc2 != 7):
            os.system('cls')                                        # Limpia pantalla.
            cInterfaz.menu_Median_of_Medians()                      # Llama método externo.
            opc2 = int(input("\nIngrese la opcion: "))              # Aquí almacenamos en opc2 lo que digite el usuario.
            #------------------------------------------------------- Bloque de evaluación para menu quicksort.
            if opc2 == 1:                                           # Opción crear Lista.
                a = self.crearLista()
            elif opc2 == 2:                                         # Opción Probar Medianas.
                os.system("cls")
                ms.median_of_medians(a,len(a)//2)
            elif opc2 == 3:                                         # Opción Probar Sort5.
                os.system("cls")
                ms.sort5(a)
            elif opc2 == 4:                                         # Opción Timing Medianas.
                os.system("cls")
            elif opc2 == 5:                                         # Opción Timind Sort5.
                os.system("cls")
            elif opc2 == 6:                                         # Opción Exportar CSV.
                os.system("cls")
            #------------------------------------------------------- Fin bloque de evaluación.
        #___________________________________________________________ Fin bloque while.
        pass

# ------------------------------------------------------------------ Bloque Principal - Main
if __name__ == "__main__":
    contr = Control()
    contr.secuencia()
    pass