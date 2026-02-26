class NodoDoble:
    def __init__(self,dato):
        self.dato= dato
        self.siguiente= None
        self.anterior= None

class ListaDoble:
    def __init__(self):
        self.cabeza = None

    def agregar(self,dato):
        nuevo = NodoDoble(dato)

        if self.cabeza == None:
            self.cabeza = nuevo
        else:
            actual= self.cabeza
            while actual.siguiente:
                actual= actual.siguiente
            actual.siguiente= nuevo
            nuevo.anterior= actual

    def mostrar(self):
        if self.cabeza is None:
            print("La lista está vacia")
        else:
            actual= self.cabeza
            while actual:
                print(actual.dato, end="--")
                actual= actual.siguiente
            print("none")
    
    # Eliminar un elemento
    def eliminar(self, dato):
        if self.cabeza is None:
            print("Lista vacía")
            return
        
        actual = self.cabeza
        
        while actual:
            if actual.dato == dato:
                # Si es el único nodo
                if actual.anterior is None and actual.siguiente is None:
                    self.cabeza = None
                # Si es la cabeza
                elif actual.anterior is None:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                # Si es el último
                elif actual.siguiente is None:
                    actual.anterior.siguiente = None
                # Nodo intermedio
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                return
            actual = actual.siguiente
        
        print("Elemento no encontrado")



# Prueba
lista = ListaDoble()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)
lista.mostrar()  # 10<->20<->30<->None
lista.eliminar(20)
lista.mostrar()