def obtain_number_from_text(texto):
    try:
        # Elimina las comas del texto
        numero_sin_comas = texto.replace(",", "")
        numero_sin_comas = numero_sin_comas.split()
        # Intenta convertir el número a entero
        numero_entero = int(numero_sin_comas[0])
        return numero_entero
    except ValueError:
        # Si no se puede convertir a entero, muestra un mensaje de error
        print("No se pudo convertir el texto a un número entero válido.")
        return None