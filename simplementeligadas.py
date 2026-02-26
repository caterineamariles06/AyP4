class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.dato == dato:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente
    def actualizar(self, viejo, nuevo):
        actual = self.cabeza
        while actual:
            if actual.dato == viejo:
                actual.dato = nuevo
                return
            actual = actual.siguiente
    








lista = ListaSimple()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

lista.mostrar()
lista.eliminar(20)
lista.mostrar()
lista.actualizar(30, 99)
lista.mostrar()
