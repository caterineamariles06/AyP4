def sumar_digitos(numero):
    # Caso base
    if numero < 10:
        return numero

    # Último dígito
    ultimo_digito = numero % 10

    # Llamada recursiva con el resto del número
    return ultimo_digito + sumar_digitos(numero // 10)

# Ejemplo de uso
numero = 12345
resultado = sumar_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")


