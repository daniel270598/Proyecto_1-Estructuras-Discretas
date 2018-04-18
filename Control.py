"""
    * Clase Control:
"""

from Interfaz import Interfaz

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
        cInterfaz = Interfaz()                                      # Creo el objeto Interfaz
        cInterfaz.menu_Principal()                                  # Llamamos al método externo.


# ------------------------------------------------------------------ Bloque Principal - Main
if __name__ == "__main__":
    Control.secuencia()
    pass