class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def eliminar_inicio(self):
        if self.esta_vacia():
            return None
        dato = self.cabeza.dato
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        return dato

    def eliminar_final(self):
        if self.esta_vacia():
            return None
        dato = self.cola.dato             # ✅ dato de la cola
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        return dato

    def recorrer_adelante(self):
        if self.esta_vacia():
            print("Lista vacía")
            return
        print("Inicio -> Fin:", end=" ")
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" <-> ".join(elementos))

    def recorrer_atras(self):
        if self.esta_vacia():
            print("Lista vacía")
            return
        print("Fin -> Inicio:", end=" ")
        actual = self.cola                # ✅ empieza desde la cola
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.anterior      # ✅ retrocede con anterior
        print(" <-> ".join(elementos))

    def buscar(self, dato):
        actual = self.cabeza              # ✅ empieza desde la cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def __len__(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def __str__(self):
        if self.esta_vacia():
            return "Lista Vacía"
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)


if __name__ == "__main__":
    lista = ListaDoble()

    lista.insertar_final(10)
    lista.insertar_final(20)
    lista.insertar_final(30)
    print(lista)                          # 10 <-> 20 <-> 30

    lista.insertar_inicio(5)
    print(lista)                          # 5 <-> 10 <-> 20 <-> 30

    lista.recorrer_adelante()             # Inicio -> Fin: 5 <-> 10 <-> 20 <-> 30
    lista.recorrer_atras()               # Fin -> Inicio: 30 <-> 20 <-> 10 <-> 5

    print(lista.eliminar_inicio())        # 5
    print(lista.eliminar_final())         # 30
    print(lista)                          # 10 <-> 20

    print(lista.buscar(10))              # True
    print(lista.buscar(99))              # False
    print(len(lista))                    # 2