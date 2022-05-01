import pandas
import re
import unidecode

def procesar_texto(texto):
    """
    Input:
        texto: una cadena de texto.

    Output: texto: una cadena de texto formada solo por las palabras del texto original, sin acentos, caracteres
    especiales o espacios extra.
    """
    # 1. Convertir el texto en minúsculas.
    texto = texto.lower()

    # 2. Eliminar acentos.
    texto = unidecode.unidecode(texto)

    # 3. Quedarnos solo con las palabras.
    texto = re.findall(r'\w+', texto)
    texto = ' '.join(texto)

    return texto
