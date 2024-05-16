import pandas as pd
def count_word_in_csv(archivo_csv, palabra):
    """
    Lee un archivo CSV y cuenta cuántas veces aparece una palabra en todas sus columnas.

    Args:
        archivo_csv (str): Ruta al archivo CSV.
        palabra (str): Palabra a buscar.

    Returns:
        int: Número total de ocurrencias de la palabra en el archivo CSV.
    """
    try:
        # Leer el archivo CSV en un DataFrame
        df = pd.read_csv(archivo_csv)

        # Filtrar las columnas que son de tipo cadena
        columnas_cadena = df.select_dtypes(include=['object']).columns

        # Contar las ocurrencias de la palabra en las columnas de tipo cadena
        total_ocurrencias = df[columnas_cadena].apply(lambda col: col.str.count(palabra)).sum().sum()

        return total_ocurrencias
    except FileNotFoundError:
        return f"El archivo '{archivo_csv}' no existe."
    except Exception as e:
        return f"Error al procesar el archivo: {str(e)}"