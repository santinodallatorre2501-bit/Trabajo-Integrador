import logica as funciones
import generador_csv as generador
import sys

def main():
    """
    Función principal. Prepara el CSV y lanza el menú.
    """
    # Chequeamos el csv
    print("Iniciando Gestor de Países...")
    # Verificamos que el generador nos devuelva lo esperado
    if not generador.garantizar_existencia_csv():
        print("El programa no puede continuar sin datos. Saliendo.")
        sys.exit(1)

    # Largamos el menú si todo salió como esperamos
    funciones.menu()

if __name__ == "__main__":
    main()