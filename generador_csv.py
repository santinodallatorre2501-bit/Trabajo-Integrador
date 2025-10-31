import requests
import csv
import sys

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
    encabezados = ["nombre", "poblacion", "superficie", "continente"]
    
    # Abrimos el archivo en modo "w" para que si el archivo csv ya existe, lo sobreescriba
    # Si no existe, lo crea
    with open(ruta_archivo, "w", newline = "", encoding = "utf-8") as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames = encabezados)
        escritor_csv.writeheader()
        for pais in paises:
            escritor_csv.writerow(pais)           
    print(f"¡Éxito! Se guardaron {len(paises)} países en {ruta_archivo}.")

def main():
    # Guardamos el retorno de obtener_datos (la lista de dicts) en una variable
    datos_paises = obtener_datos_api()
    # Verificamos que se haya devuelto la lista esperada
    if datos_paises:
        # Le pasamos a la función guardar_en_csv la lista de paises, y el nombre del archivo csv
        guardar_en_csv(datos_paises, ARCHIVO_CSV)
    else:
        # Si no se devolvió la lista esperada, terminamos el programa con un error de sistema
        print("No se pudieron obtener los datos.")
        # Terminamos con código de error
        sys.exit(1) 

# Usamos este if para que si se quiere reutilizar una función en particular, no se ejecute todo el script.
if __name__ == "__main__":
    main()