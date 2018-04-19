"""
    * Clase Control:
"""

from Interfaz import Interfaz                                       # Importa la clase Interfaz
import os                                                           # Importa para accesar al sistema.

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
    @staticmethod
    def secuencia():
        """
            * Método secuencia:
            * Método el cual se encarga de llamar a los 
            * diferentes métodos para continuar con el
            * flujo del programa.
        """
        opc = 0
        while (opc != 4):
            os.system('cls')                                        # Limpia pantalla
            cInterfaz = Interfaz()                                  # Creo el objeto Interfaz.
            cInterfaz.menu_Principal()                              # Llamamos al método externo.
            opc = int(input("\n\nIngrese la opcion: "))             # Aquí almacenamos en opc lo que digite el usuario.
            # ______________________________________________________ Bloque condicional el cual evalúa lo que
            #                                                        ingreso el usuario.
            if opc == 1:                                            # Modificar Lista
                os.system('cls')                                    # Limpia pantalla
            elif opc == 2:                                          # Submenu Quicksort.
                os.system('cls')                                    # Limpia pantalla
                cInterfaz.menu_Quicksort()                          # Llama método externo.
            elif opc == 3:                                          # Submenu Medianas.
                os.system('cls')                                    # Limpia pantalla
                cInterfaz.menu_Median_of_Medians()                  # Llama método externo.
            elif opc == 4:                                          # Salir.
                pass#exit()                                         # Sale del programa.
            # ______________________________________________________ Fin del bloque.
        pass

# ------------------------------------------------------------------ Bloque Principal - Main
if __name__ == "__main__":
    Control.secuencia()
    pass