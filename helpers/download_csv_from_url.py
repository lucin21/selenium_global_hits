import requests


def download_csv_from_url(url, nombre_archivo):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(nombre_archivo, "wb") as archivo_local:
                archivo_local.write(response.content)
            print(f"Archivo CSV descargado y guardado como '{nombre_archivo}'.")
        else:
            print(f"Error al descargar el archivo CSV. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error al descargar el archivo CSV: {e}")