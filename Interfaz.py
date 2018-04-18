"""
 
 * Clase Interfaz:

"""

class Interfaz:
    """
        * La cual desarrollara métodos de impresión 
        * para poder interactuar con el usuario.
    """
    
    # Método Constructor.
    def __init__(self):
        #self.principalMenu()
        pass

    # Método el cual imprimirá el menú principal.
    def menu_Principal(self):
        """
            * Método principalMenu:
            * Método el cual desarrollara un bloque de impresión
            * con las diferentes opciones para el usuario.
        """
        print("\n--- Bienvenido al Menu Principal ---")
        print("\n\n1. Modificar el arreglo A.")
        print("\n2. Quicksort.")
        print("\n3. Median of Medians.")
        print("\n4. Salir.")
        pass

    # Método el cual imprimirá el sub-menú para el Quicksort.
    def menu_Quicksort(self):
        pass

    # Método el cual imprimirá el sub-menú para Median of Medians.
    def menu_Median_of_Medians(self):
        pass