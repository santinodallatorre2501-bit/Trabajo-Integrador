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
            print(f"  Continente: {pais['continente']}")
            print(f"  Población: {pais['poblacion']} hab.")
            print(f"  Superficie: {pais['superficie']} kilómetros cuadrados.")
    else:
        print(f"No se encontraron países que coincidan con '{nombre_buscado}'.")

def continente_exacto(paises, continente):
    """
    Creamos una lista con los paises del continente buscado
    """
    lista_filtrada = []
    # Recorremos el csv y guardamos en una lista los países correspondientes
    for linea in paises:
        if linea["continente"] == continente:
            lista_filtrada.append((linea))
    # Devolvemos la lista filtrada
    return lista_filtrada

def pais_por_continente(paises):
    """
    Creamos un bucle para que el usuario elija el continente que quiere filtrar
    No sale del bucle hasta que elija una opción válida
    """
    print("""
1: América
2: África
3: Europa
4: Asia
5: Oceanía
""")
    valido = True
    while valido:
        opcion = input("Elija el continente: ")
        if opcion == "1":
            continente = "America"
            lista_filtrada = continente_exacto(paises, continente)
            valido = False
        elif opcion == "2":
            continente = "Africa"
            lista_filtrada = continente_exacto(paises, continente)
            valido = False
        elif opcion == "3":
            continente = "Europa"
            lista_filtrada = continente_exacto(paises, continente)
            valido = False
        elif opcion == "4":
            continente = "Asia"
            lista_filtrada = continente_exacto(paises, continente)
            valido = False
        elif opcion == "5":
            continente = "Oceania"
            lista_filtrada = continente_exacto(paises, continente)
            valido = False
        else:
            print("Ingrese un valor válido")
    return lista_filtrada

def pedir_entero_no_negativo(msg):
    """
    Pide un entero >= 0. Vuelve a pedir si el valor no es válido.
    """
    valido = True
    while valido:
        numero = input(msg)
        # Verifica que el número sea válido, si lo es, lo convierte a int
        if numero.isdigit():
            numero = int(numero)
            valido = False
        else:
            print("Ingrese un valor válido")
    # Devuelve el número convertido
    return numero 

def rangos_validos(minimo, maximo):
    """
    Verifica que el rango mínimo sea menor o igual al máximo
    """
    if minimo <= maximo:
        return True
    else:
        return False
    
def pais_por_poblacion(paises):
    """
    Creamos un bucle para que el usuario ingrese los rangos que quiere filtrar
    No sale del bucle hasta que elija rangos válidos
    """
    lista_filtrada = []
    print("Ingrese el rango mínimo y máximo a filtrar")
    valido = True
    while valido:
        # Pedimos los rangos necesarios y validamos con funciones
        rango_minimo = pedir_entero_no_negativo("Rango mínimo: ")
        rango_maximo = pedir_entero_no_negativo("Rango máximo: ")
        if rangos_validos(rango_minimo, rango_maximo):
        # Si los rangos son válidos, recorremos la lista. Sino, mensaje de error
            for pais in paises:
                # Recorremos la lista y los agregamos a la lista si cumplen con los requisitos
                if pais["poblacion"] >= rango_minimo and pais["poblacion"] <= rango_maximo:
                    lista_filtrada.append(pais)
            valido = False
        else:
            print("El rango máximo no puede ser menor que el mínimo, ingrese rangos válidos")
    # Se devuelve la lista con los países filtrados
    return lista_filtrada

def pais_por_superficie(paises):
    lista_filtrada = []
    print("Ingrese la superficie mínima y máxima a filtrar (km²)")
    valido = True
    while valido:
        # Pedimos las superficies necesarias y validamos con funciones
        superficie_minima = pedir_entero_no_negativo("Superficie mínima: ")
        superficie_maxima = pedir_entero_no_negativo("Superficie máxima: ")
        if rangos_validos(superficie_minima, superficie_maxima):
        # Si los rangos son válidos, recorremos la lista. Sino, mensaje de error
            for pais in paises:
                # Recorremos la lista y los agregamos a la lista si cumplen con los requisitos
                if pais["superficie"] >= superficie_minima and pais["superficie"] <= superficie_maxima:
                    lista_filtrada.append(pais)
            valido = False
        else:
            print("La superficie máxima no puede ser menor que la mínima, ingrese superficies válidas")
    # Se devuelve la lista con los países filtrados
    return lista_filtrada

def filtrar_paises(paises):
    """
    Desplegamos el menú del filtrado en bucle con sus correspondientes opciones
    El bucle termina solo si el usuario vuelve al menú principal
    """
    seguir = True
    while seguir:
        opcion = input(""""
--- FILTRADO DE PAISES ---
1: Filtrar país por continente
2: Filtrar país por rango de población
3: Filtrar país por rango de superficie
4: Volver al menú principal
                       
Ingrese la opción: """)
        if opcion == "1":
            # Llamamos a las funciones necesarias para hacer el filtrado por continente
            lista_resultado = pais_por_continente(paises)
            print(f"--- {len(lista_resultado)} PAÍSES ENCONTRADOS ---")
            # Recorremos la lista filtrada e imprimimos únicamente la key país de cada elemento de la lista
            for pais in lista_resultado:
                print(pais["pais"])
        elif opcion == "2":
            # Llamamos a las funciones necesarias para hacer el filtrado por población
            lista_resultado = pais_por_poblacion(paises)
            print(f"--- {len(lista_resultado)} PAÍSES ENCONTRADOS ---")
            # Recorremos la lista filtrada e imprimimos la key país y población de cada elemento de la lista
            for pais in lista_resultado:
                print(f"{pais['pais']}: {pais['poblacion']:,.0f} habitantes")
        elif opcion == "3":
            # Llamamos a las funciones necesarias para hacer el filtrado por superficie
            lista_resultado = pais_por_superficie(paises)
            print(f"--- {len(lista_resultado)} PAÍSES ENCONTRADOS ---")
            # Recorremos la lista filtrada e imprimimos la key país y superficie de cada elemento de la lista
            for pais in lista_resultado:
                print(f"{pais['pais']}: {pais['superficie']:,.0f} km²")
        elif opcion == "4":
            print("Volviendo al menú principal...")
            seguir = False
        else:
            print("Ingrese una opción correcta")

def ord_paises_por_nombre(lista_paises):
    if not lista_paises:
        print("Error, no hay datos de países cargados") #Lanza error si no existe la lista
        return
    lista_ordenada = sorted(lista_paises, key=lambda pais: pais["pais"]) #Ordena la lista alfabeticamente con el sorted
    print("Lista de paises ordenados alfabeticamente: ")
    for pais in lista_ordenada:
        print(f"Pais: {pais["pais"]} con población de {pais["poblacion"]} habitantes") #Imprime todos los paises ordenados
def ord_paises_por_poblacion(lista_paises):
    if not lista_paises:
        print("Error, no existe una lista de paises") #Lanza error si no existe la lista
        return
    lista_ordenada = sorted(lista_paises,key=lambda pais: pais["poblacion"]) #Ordena la lista según su población con el sorted
    print("Lista de paises ordenados alfabeticamente: ")
    for pais in lista_ordenada:
        print(f"Pais: {pais["pais"]} con población de {pais["poblacion"]} habitantes") #Imprime todos los paises ordenados
def ord_paises_por_superficie(lista_paises):
    if not lista_paises:
        print("Error, no existe una lista de paises") #Lanza error si no existe la lista
        return
    lista_ordenada = sorted(lista_paises,key=lambda pais: pais["superficie"]) #Ordena la lista según su superficie con el sorted
    print("Lista de paises ordenados alfabeticamente: ")
    for pais in lista_ordenada:
        print(f"Pais: {pais["pais"]} con superficie de {pais["superficie"]}") #Imprime todos los paises ordenados
def ordenar_paises(lista_paises):
    """
    Desplegamos el menú del ordenamiento en bucle con sus correspondientes opciones
    El bucle termina solo si el usuario vuelve al menú principal
    """
    seguir = True
    while seguir:
        opcion = input("""
--- ORDENAMIENTO DE PAÍSES ---
1: Ordenar países por nombre
2: Ordenar países por población
3: Ordenar países por superficie
4: Volver al menú principal
                       
Ingrese la opción: """)
        if opcion == "1":
            ord_paises_por_nombre(lista_paises)
        elif opcion == "2":
            ord_paises_por_poblacion(lista_paises)
        elif opcion == "3":
            ord_paises_por_superficie(lista_paises)
        elif opcion == "4":
            print("Volviendo al menú principal...")
            seguir = False
        else:
            print("Ingrese una opción correcta")

def mostar_mayor_poblacion(paises):
    # Establecemos el primer país de la lista como el de mayor población
    poblacion_max = paises[0]
    # Recorremos la lista de paises
    for linea in paises:
    # Si el pais de la linea actual tiene mayor población que el pais guardado en variable, reemplazamos
        if linea["poblacion"] > poblacion_max["poblacion"]:
            poblacion_max = linea
    # Devolvemos el diccionario completo del país con mayor población
    return poblacion_max

def mostrar_menor_poblacion(paises):
    # Establecemos el primer país de la lista como el de menor población
    poblacion_menor = paises[0]
    # Recorremos la lista de paises
    for linea in paises:
    # Si el pais de la linea actual tiene menor población que el pais guardado en variable, reemplazamos
        if linea["poblacion"] < poblacion_menor["poblacion"]:
            poblacion_menor = linea
     # Devolvemos el diccionario completo del país con menor población
    return poblacion_menor

def mostrar_promedio_poblacion(paises):
    # Establecemos un contador en 0
    poblacion = 0
    # Recorremos toda la lista y sumamos la key poblacion al contador
    for linea in paises:
        poblacion += linea["poblacion"]
    # Creamos una variable que divide el contador entre la longitud de la lista
    promedio = poblacion / len(paises)
    # Devolvemos únicamente la variable con el promedio
    return promedio

def mostrar_promedio_superficie(paises):
    superficie = 0
    for linea in paises:
    # Recorremos toda la lista y sumamos la key superficie al contador
        superficie += linea["superficie"]
    # Creamos una variable que divide el contador entre la longitud de la lista
    promedio = superficie / len(paises)
    # Devolvemos únicamente la variable con el promedio
    return promedio

def mostrar_cantidad_paises_continente(paises):
    # Creamos un diccionario y guardamos los continentes
    conteo = {}
    # Recorremos la lista de países y guardamos la columna 'continente' en una variable
    for linea in paises:
        continente = linea["continente"]
        # Si está en el diccionario, solo sumamos 1 a la key
        if continente in conteo:
            conteo[continente] += 1
        # Si no está, añadimos la key con valor 1
        else:
            conteo[continente] = 1
    # Devolvemos el diccionario completo
    return conteo

def mostrar_estadisticas(paises):
    """
    Desplegamos el menú de estadísticas en bucle con sus correspondientes opciones
    El bucle termina solo si el usuario vuelve al menú principal
    """
    seguir = True
    while seguir:
        opcion = input("""
--- ESTADÍSTICAS ---
1: Mostrar país con mayor población
2: Mostrar país con menor población
3: Mostrar promedio de población
4: Mostrar promedio de superficie
5: Mostrar cantidad de países por continente
6: Volver al menú principal

Ingrese la opción: """)
        if opcion == "1":
        # Llamamos a las funciones necesarias para mostrar al país con mayor población
            pais = mostar_mayor_poblacion(paises)
            print(f"""
--- PAÍS CON MAYOR POBLACIÓN ---
{pais["pais"]}: {pais["poblacion"]:,.0f} habitantes
""")
        elif opcion == "2":
        # Llamamos a las funciones necesarias para mostrar al país con menor población
            pais = mostrar_menor_poblacion(paises)
            print(f"""
--- PAÍS CON MENOR POBLACIÓN ---
{pais["pais"]}: {pais["poblacion"]:,.0f} habitantes
""")
        elif opcion == "3":
        # Llamamos a las funciones necesarias para mostrar el promedio de población
            promedio = mostrar_promedio_poblacion(paises)
            print(f"""
--- PROMEDIO DE POBLACIÓN ---
{promedio:,.0f} habitantes
""")
        elif opcion == "4":
        # Llamamos a las funciones necesarias para mostrar el promedio de superficie
            promedio = mostrar_promedio_superficie(paises)
            print(f"""
--- PROMEDIO DE SUPERFICIE ---
{promedio:,.0f} km²
""")
        elif opcion == "5":
        # Llamamos a las funciones necesarias para mostrar la cantidad de países por continente
            paises_por_continente = mostrar_cantidad_paises_continente(paises)
            print("""\n--- PAÍSES POR CONTINENTE ---""")
            # Recorremos el diccionario y usamos .items para conseguir la key y el valor e imprimimos
            # Además usamos: sorted para crear una nueva lista ordenada
            # key = lambda para un ordenado específico
            # item: item[1] para que por cada par se tome en cuenta el elemento 1 para el ordenado
            # Por defectp, lo ordena de menor a mayor, usamos reverse para que sea al revés
            for continente, cantidad in sorted(paises_por_continente.items(), key = lambda item: item[1], reverse = True):
                print(f"{continente}: {cantidad} países")
        elif opcion == "6":
            print("Volviendo al menú principal...")
            seguir = False
        else:
            print("Ingrese una opción correcta")

def menu():
    archivo = "paises.csv"
    lista_paises = cargar_csv(archivo)
    seguir = True
    while seguir:
        opcion = input("""
--- BIENVENIDO AL MENÚ DE OPCIONES ---
1: Buscar país por nombre
2: Filtrar países 
3: Ordenar paises
4: Mostrar estadísticas
5: Salir

Ingrese la opción: """)
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
