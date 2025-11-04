import requests
import csv
import sys
import os

API_URL = "https://api-paises-zilz.onrender.com/paises"
ARCHIVO_CSV = "paises.csv"


def obtener_datos_api():
    """
    Se hace la conexión con la API para obtener los datos de todos los países.
    Esto debe devolver una lista con diccionarios. 
    """
    print(f"Conectando a la API en {API_URL}...")
    try:
        # Traemos el link
        respuesta = requests.get(API_URL)

        # Verificamos que la conexión con la API sea exitosa
        if respuesta.status_code == 200:
            print("Conexión exitosa.")
            # Convertimos lo que nos entrega la API (json) en una lista de diccionarios de Python y lo devuelve 
            # Usamos la función .json, propia de python que hace la conversión
            return respuesta.json()
        else:
            # Si la API no devuelve lo esperado, devolvemos None
            return None
            
    except requests.exceptions.RequestException as e:
        # Evitamos romper el sistema por errores de conexión
        return None

def guardar_en_csv(paises, ruta_archivo):
    """
    Se guardan los datos de la API en un archivo CSV
    """
    # La propia función verifica si hay datos para guardar. 
    # Es redundante pero sirve para que la función no dependa de otras para no romper el programa.
    if not paises:
        print("No hay datos para guardar.")
        return
    print(f"Guardando datos en {ruta_archivo}")
    encabezados = ["pais", "poblacion", "superficie", "continente"]
    
    # Abrimos el archivo en modo "w" para que si el archivo csv ya existe, lo sobreescriba
    # Si no existe, lo crea
    with open(ruta_archivo, "w", newline = "", encoding = "utf-8") as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames = encabezados)
        escritor_csv.writeheader()
        for pais in paises:
            escritor_csv.writerow(pais)           
    print(f"¡Éxito! Se guardaron {len(paises)} países en {ruta_archivo}.")

def garantizar_existencia_csv():
    """
    Verifica si el CSV existe. Si no existe, lo crea desde la API.
    Devuelve True si el CSV está listo (o ya existía).
    Devuelve False si la API falló y no se pudo crear.
    """
    if not os.path.exists(ARCHIVO_CSV):
        print(f"El archivo '{ARCHIVO_CSV}' no se encontró.")
        print("Intentando generarlo automáticamente desde la API...") 
        # Llamamos al generador para traer datos de la API
        datos_api = obtener_datos_api()
        if datos_api:
            # Si la API funcionó, guardamos el CSV
            guardar_en_csv(datos_api, ARCHIVO_CSV)
            print("¡Archivo CSV generado con éxito!")
            return True 
        else:
            # Si la API falló, no podemos hacer nada.
            print("\nError: No se pudo obtener datos de la API.")
            return False
            
    # Si el if fue falso, significa que el archivo ya existía.
    # No hacemos nada y devolvemos True.
    return True

def main():
    """
    Llamamos a la función correspondiente para asegurar que el CSV exista.
    """
    print("Ejecutando generador de CSV...")
    
    if garantizar_existencia_csv():
        print("-------------------------------------")
        print("Operación completada: El archivo paises.csv está listo.")
    else:
        print("-------------------------------------")
        print("Error: Falló la creación del CSV desde la API.")
        sys.exit(1) # Termina con error si falló
        
# Usamos este if para que si se quiere reutilizar una función en particular, no se ejecute todo el script.
if __name__ == "__main__":
    main()