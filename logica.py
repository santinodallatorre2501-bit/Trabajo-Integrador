import csv
import os
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich import box
# console funciona como herramienta de la libreria rich
console = Console()

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
def limpiar_consola():
    """
    Función para limpiar la consola y se vea más prolija
    """
    # os.system ejecuta un comando de la terminal 'cls' o 'clear'
    # El if verifica si está en windows, mac o linux
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_resultados_paginados(paises, titulo = "Resultados"):
    """
    Recibe una lista de países y la muestra en tablas paginadas de a 10
    """
    # Verificamos que la lista de países no esté vacía
    if not paises:
        # Bold red le asigna al print que tiene que ir en rojo y la letra en 'negrita'
        console.print(Panel("[bold red]No se encontraron resultados[/bold red]", border_style="red"))
        input("\nPresione Enter para continuar...")
        return
    # Establecemos un contador para el nro de página y para la cantidad de items por página mostrada
    pagina_actual = 0
    items_por_pagina = 10
    # Calculamos el total de páginas
    total_paginas = (len(paises) // items_por_pagina)
    # Verificamos, después de dividir por 10, la cantidad de países que sobraron (- de 10) para tener la cant de páginas correctas
    if len(paises) % items_por_pagina != 0:
        total_paginas += 1
    # Bucle para que el usuario elija si o si una opción válida entre pág siguiente, anterior, o volver al menú
    while True:
        limpiar_consola()
        # Establecemos el inicio y el fin de cada página y lo guardamos en una variable
        inicio = pagina_actual * items_por_pagina
        fin = inicio + items_por_pagina
        pagina_a_mostrar = paises[inicio:fin]
        # Crea una tabla vacía con el título y los números de páginas
        tabla = Table(title = f"{titulo} (Página {pagina_actual + 1} de {total_paginas})")
        # Definimos las columnas y le ponemos a cada una un color, y alineación
        tabla.add_column("País", style = "cyan")
        tabla.add_column("Continente", style="magenta")
        tabla.add_column("Población", style="green", justify="right")
        tabla.add_column("Superficie (km²)", style="yellow", justify="right")
        # Recorremos la lista pero solo los 10 correspondientes
        for pais in pagina_a_mostrar:
            # Agregamos una fila a la tabla con los datos del país correspondiente
            tabla.add_row(
                pais['pais'],
                pais['continente'],
                f"{pais['poblacion']:,.0f}", # ¡Usamos el formato!
                f"{pais['superficie']:,.0f}"
            )
        # Usamos la herramienta creada para dibujar la tabla
        console.print(tabla)
        # Creamos la navegación entre las páginas y verificamos que se pueda hacer la operación que desee el usuario
        print("\n[S] Siguiente | [A] Anterior | [V] Volver al menú")
        opcion = input("Opción: ").lower()
        if opcion == "s":
            if (pagina_actual + 1) < total_paginas:
                pagina_actual += 1
            else:
                input("Estás en la última página. (Enter para continuar)")
        elif opcion == "a":
            if pagina_actual > 0:
                pagina_actual -= 1
            else:
                input("Estás en la primera página. (Enter para continuar)")
        elif opcion == "v":
            break # Sale del bucle de paginación
        else:
            console.print(Panel("[bold red]Opción no válida.[/bold red]", border_style="red"))
            input("\nPresione Enter para continuar...")

def paises_por_nombre(lista_paises):
    """
    (Opción 1)
    Busca país por nombre parcial y muestra los resultados en una tabla.
    """
    limpiar_consola()
    if not lista_paises:
        # Usamos 'Console' para imprimir el error en rojo
        Console().print("Error: No hay datos de países cargados.", style="bold red")
        input("\nPresione Enter para continuar...")
        return [], ""

    nombre_buscado = Prompt.ask("[bold magenta]Ingrese el nombre del país a buscar[/bold magenta]")
    if nombre_buscado:
    
        nombre_buscado_lower = nombre_buscado.lower()

        resultados = []
        for pais in lista_paises:
            nombre_pais_lower = pais.get('pais', '').lower()

            if nombre_buscado_lower in nombre_pais_lower:
                resultados.append(pais)
        return resultados, nombre_buscado

    else: 
        return [], nombre_buscado

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
    # Llamamos a la función para limpiar consola
    limpiar_consola()
    menu = """
[bold]1:[/bold] América
[bold]2:[/bold] África
[bold]3:[/bold] Europa
[bold]4:[/bold] Asia
[bold]5:[/bold] Oceanía
"""
    valido = True
    while valido:
        limpiar_consola()
        # Align permite alinear el cuadro que hagamos con panel
        # Border style el color del borde
        # Box para elegir tipo de borde
        console.print(Align.left(Panel(menu, title = " CONTINENTES ", border_style = "magenta", box = box.ROUNDED)))
        # Prompt.ask() reemplaza a input() y permite estilos
        opcion = Prompt.ask("\n[bold magenta]Elija el continente[/bold magenta]")
        if opcion == "1":
            # Llamamos a la función para limpiar consola
            limpiar_consola()
            continente = "America"
            lista_filtrada = continente_exacto(paises, continente)
            valido = False
        elif opcion == "2":
            # Llamamos a la función para limpiar consola
            limpiar_consola()
            continente = "Africa"
            lista_filtrada = continente_exacto(paises, continente)
            valido = False
        elif opcion == "3":
            # Llamamos a la función para limpiar consola
            limpiar_consola()
            continente = "Europa"
            lista_filtrada = continente_exacto(paises, continente)
            valido = False
        elif opcion == "4":
            # Llamamos a la función para limpiar consola
            limpiar_consola()
            continente = "Asia"
            lista_filtrada = continente_exacto(paises, continente)
            valido = False
        elif opcion == "5":
            continente = "Oceania"
            lista_filtrada = continente_exacto(paises, continente)
            valido = False
        else:
            console.print(Align.left(Panel("[bold red]Ingrese una opción correcta.[/bold red]", border_style="red", box = box.HEAVY)))
            input("\nPresione Enter para continuar...")
    return lista_filtrada

def pedir_entero_no_negativo(msg):
    """
    Pide un entero >= 0. Vuelve a pedir si el valor no es válido.
    """
    valido = True
    while valido:
        # IntPrompt para darle formato al mensaje
        numero = Prompt.ask(msg)
        # Verifica que el número sea mayor o igual que 0. IntPrompt ya se asegura de que sea un entero
        if numero.isdigit():
            numero = int(numero)
            valido = False
        else:
           console.print(Align.left(Panel("[bold red]Ingrese un valor válido.[/bold red]", border_style="red", box = box.HEAVY)))
           input("\nPresione Enter para continuar...")
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
    # Align permite alinear el cuadro que hagamos con panel
    # Border style el color del borde
    # Box para elegir tipo de borde
    valido = True
    while valido:
        limpiar_consola()
        # Pedimos los rangos necesarios y validamos con funciones
        console.print(Align.left(Panel("[bold magenta]Ingrese el rango mínimo y máximo a filtrar[/bold magenta]", border_style = "magenta", box = box.ROUNDED)))
        rango_minimo = pedir_entero_no_negativo("[bold magenta]Rango mínimo[/bold magenta]")
        rango_maximo = pedir_entero_no_negativo("[bold magenta]Rango máximo[/bold magenta]")
        if rangos_validos(rango_minimo, rango_maximo):
        # Si los rangos son válidos, recorremos la lista. Sino, mensaje de error
            for pais in paises:
                # Recorremos la lista y los agregamos a la lista si cumplen con los requisitos
                if pais["poblacion"] >= rango_minimo and pais["poblacion"] <= rango_maximo:
                    lista_filtrada.append(pais)
            valido = False
        else:
            console.print(Align.left(Panel("[bold red]El rango máximo no puede ser menor que el mínimo, ingrese rangos válidos[/bold red]", border_style="red")))
            input("\nPresione Enter para continuar...")
    # Se devuelve la lista con los países filtrados
    return lista_filtrada

def pais_por_superficie(paises):
    """
    Creamos un bucle para que el usuario ingrese los rangos que quiere filtrar
    No sale del bucle hasta que elija rangos válidos
    """
    lista_filtrada = []
    # Align permite alinear el cuadro que hagamos con panel
    # Border style el color del borde
    # Box para elegir tipo de borde
    valido = True
    while valido:
        limpiar_consola()
        # Pedimos las superficies necesarias y validamos con funciones
        console.print(Align.left(Panel("[bold magenta]Ingrese la superficie mínima y máxima a filtrar (km²)[/bold magenta]", border_style = "magenta", box = box.ROUNDED)))
        superficie_minima = pedir_entero_no_negativo("[bold magenta]Superficie mínima[/bold magenta]")
        superficie_maxima = pedir_entero_no_negativo("[bold magenta]Superficie máxima[/bold magenta]")
        if rangos_validos(superficie_minima, superficie_maxima):
        # Si los rangos son válidos, recorremos la lista. Sino, mensaje de error
            for pais in paises:
                # Recorremos la lista y los agregamos a la lista si cumplen con los requisitos
                if pais["superficie"] >= superficie_minima and pais["superficie"] <= superficie_maxima:
                    lista_filtrada.append(pais)
            valido = False
        else:
            console.print(Align.left(Panel("[bold red]La superficie máxima no puede ser menor que la mínima, ingrese superficies válidas[/bold red]", border_style="red")))
            input("\nPresione Enter para continuar...")
    # Se devuelve la lista con los países filtrados
    return lista_filtrada

def filtrar_paises(paises):
    """
    Desplegamos el menú del filtrado en bucle con sus correspondientes opciones
    El bucle termina solo si el usuario vuelve al menú principal
    """
    seguir = True
    while seguir:
        # Llamamos a la función para limpiar consola
        limpiar_consola()
        menu = """
[bold]1:[/bold] Filtrar país por continente
[bold]2:[/bold] Filtrar país por rango de población
[bold]3:[/bold] Filtrar país por rango de superficie
[bold]4:[/bold] Volver al menú principal
"""
        # Align permite alinear el cuadro que hagamos con panel
        # Border style el color del borde
        # Box para elegir tipo de borde
        console.print(Align.left(Panel(menu, title = " FILTRADO DE PAÍSES ", border_style = "cyan", box = box.ROUNDED)))
        # Prompt.ask() reemplaza a input() y permite estilos
        opcion = Prompt.ask("\n[bold cyan]Ingrese la opción[/bold cyan]")
        if opcion == "1":
            # Llamamos a las funciones necesarias para hacer el filtrado por continente
            lista_resultado = pais_por_continente(paises)
            # Mostramos el resultado en una tabla
            mostrar_resultados_paginados(lista_resultado, "Filtro por continente")
        elif opcion == "2":
            # Llamamos a las funciones necesarias para hacer el filtrado por población
            lista_resultado = pais_por_poblacion(paises)
            # Mostramos el resultado en una tabla
            mostrar_resultados_paginados(lista_resultado, "Filtro por población")
        elif opcion == "3":
            # Llamamos a las funciones necesarias para hacer el filtrado por superficie
            lista_resultado = pais_por_superficie(paises)
            # Mostramos el resultado en una tabla
            mostrar_resultados_paginados(lista_resultado, "Filtro por superficie")
        elif opcion == "4":
            Console().print("Volviendo al menú principal...", style = "bold yellow")
            seguir = False
        else:
            console.print(Align.left(Panel("[bold red]Ingrese una opción correcta.[/bold red]", border_style="red", box = box.HEAVY)))
            input("\nPresione Enter para continuar...")

def ord_paises_por_nombre(lista_paises):
    if not lista_paises:
        Console().print("Error: No hay datos de países cargados.", style="bold red") #Lanza error si no existe la lista
        return
    lista_ordenada = sorted(lista_paises, key=lambda pais: pais["pais"]) #Ordena la lista alfabeticamente con el sorted
    return lista_ordenada

def ord_paises_por_poblacion(lista_paises):
    if not lista_paises:
        Console().print("Error: No hay datos de países cargados.", style="bold red") #Lanza error si no existe la lista
        return
    lista_ordenada = sorted(lista_paises,key=lambda pais: pais["poblacion"]) #Ordena la lista según su población con el sorted
    return lista_ordenada

def ord_paises_por_superficie(lista_paises):
    if not lista_paises:
        Console().print("Error: No hay datos de países cargados.", style="bold red") #Lanza error si no existe la lista
        return
    lista_ordenada = sorted(lista_paises,key=lambda pais: pais["superficie"]) #Ordena la lista según su superficie con el sorted
    return lista_ordenada


def ordenar_paises(lista_paises):
    """
    Desplegamos el menú del ordenamiento en bucle con sus correspondientes opciones
    El bucle termina solo si el usuario vuelve al menú principal
    """
    seguir = True
    while seguir:
        # Llamamos a la función para limpiar consola
        limpiar_consola()
        menu = """
[bold]1:[/bold] Ordenar países por nombre
[bold]2:[/bold] Ordenar países por población
[bold]3:[/bold] Ordenar países por superficie
[bold]4:[/bold] Volver al menú principal
"""
        # Align permite alinear el cuadro que hagamos con panel
        # Border style el color del borde
        # Box para elegir tipo de borde
        console.print(Align.left(Panel(menu, title = " ORDENAMIENTO DE PAÍSES ", border_style = "cyan", box = box.ROUNDED)))
        # Prompt.ask() reemplaza a input() y permite estilos
        opcion = Prompt.ask("\n[bold cyan]Ingrese la opción[/bold cyan]")
        if opcion == "1":
            lista_ordenada = ord_paises_por_nombre(lista_paises)
            mostrar_resultados_paginados(lista_ordenada, "Orden por nombre")
        elif opcion == "2":
            lista_ordenada = ord_paises_por_poblacion(lista_paises)
            mostrar_resultados_paginados(lista_ordenada, "Orden por población")
        elif opcion == "3":
            lista_ordenada = ord_paises_por_superficie(lista_paises)
            mostrar_resultados_paginados(lista_ordenada, "Orden por superficie")
        elif opcion == "4":
            Console().print("Volviendo al menú principal...", style = "bold yellow")
            seguir = False
            return []
        else:
            console.print("[bold red]Ingrese una opción correcta[/bold red]")
            input("\nPresione Enter para continuar...")
    return lista_ordenada

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
        # Llamamos a la función para limpiar consola
        limpiar_consola()
        # Creamos una variable para desplegar el menú con bold (letra negrita y con color)
        menu = """
[bold]1:[/bold] Mostrar país con mayor población
[bold]2:[/bold] Mostrar país con menor población
[bold]3:[/bold] Mostrar promedio de población
[bold]4:[/bold] Mostrar promedio de superficie
[bold]5:[/bold] Mostrar cantidad de países por continente
[bold]6:[/bold] Volver al menú principal
"""
        # Align permite alinear el cuadro que hagamos con panel
        # Border style el color del borde
        # Box para elegir tipo de borde
        console.print(Align.left(Panel(menu, title = " ESTADÍSTICAS ", border_style = "blue", box = box.DOUBLE)))
        # Prompt.ask() reemplaza a input() y permite estilos
        opcion = Prompt.ask("\n[bold blue]Ingrese la opción[/bold blue]")
        if opcion == "1":
        # Llamamos a las funciones necesarias para mostrar al país con mayor población
            pais = mostar_mayor_poblacion(paises)
        # Desplegamos un panel que muestra los resultados con colores
            resultado_texto = f"[magenta] {pais['pais']}:[/magenta] [white] {pais['poblacion']:,.0f} [/white] habitantes"
            # Agregamos un print vacío para forzar un salto de línea
            console.print()
            console.print(Align.left(Panel(resultado_texto, title = " PAÍS CON MAYOR POBLACIÓN ", border_style = "magenta")))
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
        # Llamamos a las funciones necesarias para mostrar al país con menor población
            pais = mostrar_menor_poblacion(paises)
        # Desplegamos un panel que muestra los resultados con colores
            resultado_texto = f"[magenta] {pais['pais']}:[/magenta] [white] {pais['poblacion']:,.0f} [/white] habitantes"
            # Agregamos un print vacío para forzar un salto de línea
            console.print()
            console.print(Align.left(Panel(resultado_texto, title = " PAÍS CON MENOR POBLACIÓN ", border_style = "magenta")))
            input("\nPresione Enter para continuar...")
        elif opcion == "3":
        # Llamamos a las funciones necesarias para mostrar el promedio de población
            promedio = mostrar_promedio_poblacion(paises)
        # Desplegamos un panel que muestra los resultados con colores
            resultado_texto = f"El promedio de población mundial es: [magenta]{promedio:,.0f} habitantes[/magenta]"
            # Agregamos un print vacío para forzar un salto de línea
            console.print()
            console.print(Align.left(Panel(resultado_texto, title = " PROMEDIO DE POBLACIÓN ", border_style = "magenta")))
            input("\nPresione Enter para continuar...")
        elif opcion == "4":
        # Llamamos a las funciones necesarias para mostrar el promedio de superficie
            promedio = mostrar_promedio_superficie(paises)
        # Desplegamos un panel que muestra los resultados con colores
            resultado_texto = f"El promedio de superficie mundial es: [magenta]{promedio:,.0f} km²[/magenta]"
            console.print()
            console.print(Align.left(Panel(resultado_texto, title = " PROMEDIO DE SUPERFICIE ", border_style = "magenta")))
            input("\nPresione Enter para continuar...")
        elif opcion == "5":
        # Llamamos a las funciones necesarias para mostrar la cantidad de países por continente
            paises_por_continente = mostrar_cantidad_paises_continente(paises)
        # Usamos una tabla para mostrar los resultados
        # Definimos el titulo, sus columnas, los colores de ellas y alineación
            tabla_conteo = Table(title = "--- PAÍSES POR CONTINENTE ---")
            tabla_conteo.add_column("Continente", style = "magenta")
            tabla_conteo.add_column("Cantidad de Países", style = "green", justify = "right")
            # Recorremos el diccionario y usamos .items para conseguir la key y el valor e imprimimos
            # Además usamos: sorted para crear una nueva lista ordenada
            # key = lambda para un ordenado específico
            # item: item[1] para que por cada par se tome en cuenta el elemento 1 para el ordenado
            # Por defecto, lo ordena de menor a mayor, usamos reverse para que sea al revés
            for continente, cantidad in sorted(paises_por_continente.items(), key=lambda item: item[1], reverse=True):
                tabla_conteo.add_row(continente, str(cantidad))
            console.print(tabla_conteo)
            input("\nPresione Enter para continuar...")
        elif opcion == "6":
            Console().print("Volviendo al menú principal...", style = "bold yellow")
            seguir = False
        else:
            console.print("[bold red]Ingrese una opción correcta[/bold red]")
            input("\nPresione Enter para continuar...")

def menu():
    archivo = "paises.csv"
    lista_paises = cargar_csv(archivo)
    seguir = True
    while seguir:
        # Llamamos a la función para limpiar consola
        limpiar_consola()
        menu = """
[bold]1:[/bold] Buscar país por nombre
[bold]2:[/bold] Filtrar países
[bold]3:[/bold] Ordenar paises
[bold]4:[/bold] Mostrar estadísticas
[bold]5:[/bold] Salir
"""
        # Align permite alinear el cuadro que hagamos con panel
        # Border style el color del borde
        # Box para elegir tipo de borde
        console.print(Align.left(Panel(menu, title = " MENÚ DE OPCIONES ", border_style = "blue", box = box.DOUBLE)))
        # Prompt.ask() reemplaza a input() y permite estilos
        opcion = Prompt.ask("\n[bold blue]Ingrese la opción[/bold blue]")
        if opcion == "1":
            resultados, pais = paises_por_nombre(lista_paises)
            mostrar_resultados_paginados(resultados, f"Resultados para: {pais}")
        elif opcion == "2":
            filtrar_paises(lista_paises)
            input("\nPresione Enter para continuar...")
        elif opcion == "3":
            ordenar_paises(lista_paises)
            input("\nPresione Enter para continuar...")
        elif opcion == "4":
            mostrar_estadisticas(lista_paises)
            input("\nPresione Enter para continuar...")
        elif opcion == "5":
            limpiar_consola()
            console.print(Align.left(Panel("[bold medium_purple]Gracias por usar nuestro menú. Saliendo del programa...[/bold medium_purple]", border_style="medium_purple", box = box.DOUBLE)))
            input("\nPresione Enter para salir...")
            seguir = False
        else:
            console.print(Align.left(Panel("[bold red]Ingrese una opción correcta.[/bold red]", border_style="red", box = box.HEAVY)))
            input("\nPresione Enter para continuar...")