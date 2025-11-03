import csv

def cargar_csv(archivo_csv):
    """
    Lee el CSV y lo pasa a una lista de diccionarios.
    Transforma los números a int para podes manejarlos.
    """
    lista_paises = []
    with open(archivo_csv, "r", newline = "", encoding = "utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for linea in lector:
            try:
                # Pasamos a int los números del diccionario
                linea["poblacion"] = int(linea["poblacion"])
                linea["superficie"] = int(linea["superficie"])
                lista_paises.append(linea)
            except ValueError:
                # Validamos que "poblacion" o "superficie" tenga un número válido.
                print(f"Error de formato en datos de {linea['pais']}. Se omite")
            except KeyError:
                # Validamos que la columna del CSV se llama como esperamos
                print(f"Error  de columna en CSV. Se omite fila")
    return lista_paises
def paises_por_nombre(lista_paises):
    if not lista_paises:
        print("Error: No hay datos de países cargados.")
        return

    nombre_buscado = input("Ingrese el nombre del país a buscar: ")
    
    # Convertimos la búsqueda a minúsculas para que no importe (case-insensitive)
    nombre_buscado_lower = nombre_buscado.lower()
    
    resultados = []
    for pais in lista_paises:
        nombre_pais_lower = pais.get('pais', '').lower()
        
        # Comprobamos si el texto buscado está dentro del nombre del país
        if nombre_buscado_lower in nombre_pais_lower:
            resultados.append(pais)

    # Fuera del bucle, mostramos los resultados
    if resultados:
        print(f"\n--- {len(resultados)} Países Encontrados ---")
        # Usamos un bucle para imprimir los resultados de forma bonita
        for pais in resultados:
            print(f"  País: {pais['pais']}") 
            print(f"    Continente: {pais['continente']}")
            print(f"    Población: {pais['poblacion']} hab.")
            print(f"    Superficie: {pais['superficie']} kilómetros cuadrados.")
    else:
        print(f"No se encontraron países que coincidan con '{nombre_buscado}'.")

def pais_por_continente():
    pass
def pais_por_poblacion():
    pass
def pais_por_superficie():
    pass
def ord_paises_por_nombre():
    pass
def ord_paises_por_poblacion():
    pass
def ord_paises_por_superficie():
    pass
def mostar_mayor_poblacion():
    pass
def mostrar_menor_poblacion():
    pass
def mostrar_promedio_poblacion():
    pass
def mostrar_promedio_superficie():
    pass
def mostrar_cantidad_paises_continente():
    pass
def filtrar_paises():
    opcion = 0
    print("""
1: Filtrar país Por continente
2: Filtrar país por rango de población
3: Filtrar país por rango de superficie
4: Volver al menú principal
""")
    seguir = True
    while seguir:
        opcion = input("Ingrese la opción: ")
        if opcion == "1":
            pais_por_continente()
        elif opcion == "2":
            pais_por_poblacion()
        elif opcion == "3":
            pais_por_superficie()
        elif opcion == "4":
            seguir = False
        else:
            print("Ingrese una opción correcta")
def ordenar_paises():
    opcion = 0
    print("""
1: Ordenar países por nombre
2: Ordenar países por población
3: Ordenar países por superficie
4: Volver al menú principal
""")
    seguir = True
    while seguir:
        opcion = input("Ingrese la opción: ")
        if opcion == "1":
            ord_paises_por_nombre()
        elif opcion == "2":
            ord_paises_por_poblacion()
        elif opcion == "3":
            ord_paises_por_superficie()
        elif opcion == "4":
            seguir = False
        else:
            print("Ingrese una opción correcta")
def mostrar_estadisticas():
    opcion = 0
    print("""
1: Mostrar país con mayor población
2: Mostrar país con menor población
3: Mostrar promedio de población
4: Mostrar promedio de superficie
5: Mostrar cantidad de países por continente
6: Volver al menú principal
""")
    seguir = True
    while seguir:
        opcion = input("Ingrese la opción: ")
        if opcion == "1":
            mostar_mayor_poblacion()
        elif opcion == "2":
            mostrar_menor_poblacion()
        elif opcion == "3":
            mostrar_promedio_poblacion()
        elif opcion == "4":
            mostrar_promedio_superficie()
        elif opcion == "5":
            mostrar_cantidad_paises_continente()
        elif opcion == "6":
            seguir = False
        else:
            print("Ingrese una opción correcta")

def menu():
    archivo = "paises.csv"
    lista_paises = cargar_csv(archivo)
    seguir = True
    while seguir:
        opcion = 0
        print("""
    --- BIENVENIDO AL MENÚ DE OPCIONES ---
    1:  Buscar país por nombre
    2:  Filtrar países 
    3: Ordenar paises
    4: Mostrar estadísticas
    5: Salir
    """)
        opcion = input("Ingrese la opción: ")
        if opcion == "1":
            paises_por_nombre(lista_paises)
        elif opcion == "2":
            filtrar_paises(lista_paises)
        elif opcion == "3":
            ordenar_paises(lista_paises)
        elif opcion == "4":
            mostrar_estadisticas(lista_paises)
        elif opcion == "5":
            print("Gracias por usar nuestro menú. Saliendo del programa...")
            seguir = False
        else:
            print("Ingrese una opción correcta")

menu()
