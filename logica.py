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
def paises_por_nombre():
    pass
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


def menu():
    opcion = 0
    print("""
--- BIENVENIDO AL MENÚ DE OPCIONES ---
1:  Buscar país por nombre
2:  Filtrar país por continente
3:  Filtrar país por rango de población
4:  Filtrar país por rango de superficie
5:  Ordenar países por nombre
6:  Ordenar países por población
7:  Ordenar países por superficie
8:  Mostrar país con mayor población
9:  Mostrar país con menor población
10: Mostrar promedio de población
11: Mostrar promedio de superficie
12: Mostrar cantidad de países por continente
13:  Salir
""")
    opcion = int(input("Ingrese la opcion: "))

cargar_csv()
menu()
