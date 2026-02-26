def busqueda_binaria(lista, num, inicio, fin):
    # Caso base: no encontrado
    if inicio > fin:
        return -1

    # Calcular la mitad
    medio = (inicio + fin) // 2

    # Caso: encontrado
    if lista[medio] == num:
        return medio

    # Buscar en la mitad izquierda
    elif num < lista[medio]:
        return busqueda_binaria(lista, num, inicio, medio - 1)

    # Buscar en la mitad derecha
    else:
        return busqueda_binaria(lista, num, medio + 1, fin)
    
# Ejemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
numero_a_buscar = 9

resultado = busqueda_binaria(lista_ordenada, numero_a_buscar, 0, len(lista_ordenada) - 1)