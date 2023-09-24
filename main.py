import random  # Importa el módulo random para generar números aleatorios y selecciones aleatorias.
import string  # Importa el módulo string para trabajar con cadenas de caracteres.

# Implementación del algoritmo de ordenamiento Merge Sort
def merge_sort(lista, inicio=0, fin=None):
    if fin is None:  # Si fin no está especificado, establece fin como la longitud de la lista.
        fin = len(lista)

    if fin - inicio <= 1:  # Si la porción de la lista es de tamaño 0 o 1, está ordenada por definición.
        return lista[inicio:fin]  # Devuelve la sublista.

    # Divide la lista en dos mitades y ordena cada mitad recursivamente.
    mitad = (fin + inicio) // 2
    izquierda = merge_sort(lista, inicio, mitad)
    derecha = merge_sort(lista, mitad, fin)

    # Combina las dos mitades ordenadas.
    return merge(izquierda, derecha)

# Función para combinar dos listas ordenadas
def merge(izquierda, derecha):
    resultado = []  # Lista para almacenar el resultado combinado de las dos listas ordenadas.

    # Combina las dos listas ordenadas seleccionando el elemento más pequeño en cada iteración.
    while (izquierda and derecha):
        if izquierda[0] < derecha[0]:
            resultado.append(izquierda[0])
            izquierda.pop(0)  # Elimina el elemento ya procesado de la lista izquierda.
        else:
            resultado.append(derecha[0])
            derecha.pop(0)  # Elimina el elemento ya procesado de la lista derecha.

    # Agrega los elementos restantes de izquierda y derecha.
    if izquierda:
        resultado += izquierda
    if derecha:
        resultado += derecha

    return resultado  # Devuelve la lista combinada y ordenada.

# Punto de entrada del programa
if __name__ == "__main__":
    # Genera una lista de 500 documentos aleatorios, cada uno con 5 letras minúsculas aleatorias.
    documentos = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(500)]

    # Ordena una porción de la lista de documentos (índices 100 a 199) usando Merge Sort.
    documentos_ordenados = merge_sort(documentos, 0, 499)

    # Imprime cada documento ordenado.
    for documento in documentos_ordenados:
        print(documento)