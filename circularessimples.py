class Nodo:
    def __init__(self,dato):
        self.dato= dato
        self.siguiente= None
        self.anterior= None
class ListaCircular:
    def __init__(self):
        self.cabeza = None
    
    # Agregar al final
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
    
    # Agregar al inicio
    def agregar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            
            nuevo_nodo.siguiente = self.cabeza
            actual.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo
    
    # Eliminar
    def eliminar(self, dato):
        if self.cabeza is None:
            print("Lista vacía")
            return
        
        # Si solo hay un nodo
        if self.cabeza.dato == dato and self.cabeza.siguiente == self.cabeza:
            self.cabeza = None
            return
        
        # Si la cabeza es el nodo a eliminar
        if self.cabeza.dato == dato:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
            return
        
        # Buscar el nodo a eliminar
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
        
        print("Elemento no encontrado")
    
    # Buscar
    def buscar(self, dato):
        if self.cabeza is None:
            return -1
        
        actual = self.cabeza
        posicion = 0
        
        while True:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
            if actual == self.cabeza:
                break
        
        return -1
    
    # Actualizar
    def actualizar(self, dato_viejo, dato_nuevo):
        if self.cabeza is None:
            return False
        
        actual = self.cabeza
        
        while True:
            if actual.dato == dato_viejo:
                actual.dato = dato_nuevo
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        
        return False
    
    # Mostrar
    def mostrar(self):
        if self.cabeza is None:
            print("Lista vacía")
            return
        
        elementos = []
        actual = self.cabeza
        
        while True:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        
        print(" -> ".join(elementos) + " -> (regresa a " + elementos[0] + ")")
    
    # Longitud
    def longitud(self):
        if self.cabeza is None:
            return 0
        
        contador = 1
        actual = self.cabeza.siguiente
        
        while actual != self.cabeza:
            contador += 1
            actual = actual.siguiente
        
        return contador

# Ejemplo de uso
print("\n=== LISTA CIRCULAR ===")
lista_circular = ListaCircular()
lista_circular.agregar(10)
lista_circular.agregar(20)
lista_circular.agregar(30)
lista_circular.agregar_inicio(5)

lista_circular.mostrar()  # 5 -> 10 -> 20 -> 30 -> (regresa a 5)

lista_circular.eliminar(20)
lista_circular.mostrar()  # 5 -> 10 -> 30 -> (regresa a 5)

lista_circular.actualizar(10, 15)
lista_circular.mostrar()  # 5 -> 15 -> 30 -> (regresa a 5)

print(f"Longitud: {lista_circular.longitud()}")