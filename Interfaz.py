"""
 
 * Clase Interfaz:

"""

class Interfaz:
    """
        * La cual desarrollara métodos de impresión 
        * para poder interactuar con el usuario.
    """

    # Método el cual imprimirá el menú principal.
    def menu_Principal(self):
        """
            * Método principalMenu:
            * Método el cual desarrollara un bloque de impresión
            * con las diferentes opciones para el usuario.
        """
        print("\n--- Bienvenido al Menu Principal ---")
        print("\n1. Quicksort.")
        print("2. Median of Medians.")
        print("\n3. Salir.")
        pass

    # Método el cual imprimirá el sub-menú para el Quicksort.
    def menu_Quicksort(self):
        """
            * Método menu_Quicksort:
            * Método el cual desarrollara un bloque de impresión
            * con las diferentes opciones para el usuario en base a el Quicksort.
        """
        print("\n--- Bienvenido al Menu Quicksort ---")
        print("\n1. Modificar el arreglo A.")
        print("2. Quicksort.")
        print("3. Median of Medians.")
        print("\n4. Salir.")
        pass

    # Método el cual imprimirá el sub-menú para Median of Medians.
    def menu_Median_of_Medians(self):
        """
            * Método menu_Median_of_Medians:
            * Método el cual desarrollara un bloque de impresión
            * con las diferentes opciones para el usuario en base a el Median_of_Medians.
        """
        print("\n--- Bienvenido al Menu Median_of_Medians ---")
        print("\n1. Crear Lista.")
        print("2. Prueba de Medianas")
        print("3. Prueba de sort5.")
        print("4. Timing Medianas.")
        print("5. Timing sort5.")
        print("\n6. Salir.")
        pass