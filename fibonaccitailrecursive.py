def fibonacci(n):
    # Caso base
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Llamada recursiva con el resultado de la función para n-1 y n-2
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_tail_recursive(n, actual=0,siguiente=1):
    if n == 0:
        return actual
    return fibonacci_tail_recursive(n - 1, siguiente, actual + siguiente)

import time
inicio = time.time() # Toma la hora actual antes de la ejecución
print(fibonacci(4)) 
print(time.time() - inicio) # Imprime el tiempo transcurrido desde el inicio