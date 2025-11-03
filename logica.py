def cargar_csv():
    pass

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
0:  Salir
""")
    opcion = int(input("Ingrese la opcion: "))

cargar_csv()
menu()
