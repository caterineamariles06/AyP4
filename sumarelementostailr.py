def suma_lista(lista, acumulador=0):
    # Caso base: lista vacía
    if len(lista) == 0:
        return acumulador

    # Sumar el primer elemento con la suma del resto de la lista
    return suma_lista(lista[1:], acumulador + lista[0]) # Llamada recursiva con el resto de la lista y el acumulador actualizado

def potencia_tail(base, exponente, acumulador=1):
    # Caso base: exponente es 0
    if exponente == 0:
        return acumulador

    # Multiplicar la base por la potencia de la base con el exponente reducido en 1
    return potencia_tail(base, exponente - 1, acumulador * base) # Llamada recursiva con el exponente reducido y el acumulador actualizado


def potencia(base, exponente):
    # Caso base: exponente es 0
    if exponente == 0:
        return 1

    # Multiplicar la base por la potencia de la base con el exponente reducido en 1
    return base * potencia(base, exponente - 1) # Llamada recursiva con el exponente reducido   


# Ejemplo de uso
print(potencia(2, 3)) # Imprime 8
print(potencia_tail(2, 3)) # Imprime 8