print("Try programiz.pro")
"""Una librería necesita gestionar su inventario.
Cada libro tiene: titulo, autor, precio (int), vendido (True/False)

LISTA SIMPLE

PUNTO 1 - ESTRUCTURAS:
Diseñá las clases Libro y Libreria.
Los libros se ordenan por precio (mayor primero).

PUNTO 2 - AGREGAR ORDENADO (recursivo):
Ejemplo:
  Lista: [50000, 30000, 10000]
  Agrego 40000 → [50000, 40000, 30000, 10000]

PUNTO 3 - CALCULAR RECAUDACION (recursivo):
Sumá el precio de todos los libros YA vendidos.
Ejemplo:
  calcular_recaudacion() → 80000

PUNTO 4 - OBTENER BARATOS (recursivo):
Retorná una NUEVA lista con libros de precio menor a X
que NO estén vendidos.
Ejemplo:
  baratos = libreria.obtener_baratos(20000)

PUNTO 5 - LIMPIAR VENDIDOS (recursivo):
Eliminá todos los libros vendidos de la lista original.
  Antes:  [✓]Libro1 -> [○]Libro2 -> [✓]Libro3
  Después: [○]Libro2"""
  
 
class Libro:
    def __init__(self,titulo, autor, precio):
        self.titulo=titulo
        self.autor= autor
        self.precio= precio
        self.vendido= False
        self.siguiente= None
class Libreria:
    def __init__(self):
        self.inicio= None
    
    def agregar_libro(self, titulo, autor, precio):
        nuevo= Libro(titulo, autor, precio)
        if self.inicio is None or self.inicio.precio < nuevo.precio:
            nuevo.siguiente= self.inicio
            self.inicio= nuevo
        else:
            self._agregar_libro(self.inicio, nuevo)
            
    def _agregar_libro(self, nodo, nuevo):
        if nodo.siguiente is None or nodo.siguiente.precio < nuevo.precio:
            nuevo.siguiente= nodo.siguiente
            nodo.siguiente=nuevo
        else:
            self._agregar_libro(nodo.siguiente, nuevo)
            
    def calcular_recaudacion(self):
        return self._calcular_recaudacion(self.inicio)
        
    def _calcular_recaudacion(self, nodo):
        if nodo is None:
            return 0
        return nodo.precio + (self._calcular_recaudacion(nodo.siguiente))
        
    def obtener_baratos(self, maximo):
        nueva_lista=Libreria()
        return self._obtener_baratos(self.inicio, nueva_lista, maximo)
    def _obtener_baratos(self,nodo, lista, maximo):
        if nodo is None:
            return lista
        if nodo.precio < maximo and not nodo.vendido:
            lista.agregar_libro(nodo.titulo, nodo.autor, nodo.precio)
        return self._obtener_baratos(nodo.siguiente, lista, maximo)

        
    def limpiar_vendidos(self):
        self.inicio=self._limpiar_vendidos(self.inicio)
        
    def _limpiar_vendidos(self, nodo):
        if nodo is None:
            return None 
        if nodo.vendido:
            return self._limpiar_vendidos(nodo.siguiente)
        nodo.siguiente=self._limpiar_vendidos(nodo.siguiente)
        return nodo
    
    def mostrar(self):
        actual=self.inicio
        if actual is None:
            print ("Carrito vacio")
            return
        while actual:
            print(f"🔗 {actual.titulo} | {actual.autor} | {actual.precio}")
            actual = actual.siguiente
    
    def marcar_vendido(self, nombre):
        actual=self.inicio
        while actual:
            if actual.titulo==nombre:
                actual.vendido= True
                return
            actual=actual.siguiente
        
if __name__ == "__main__":
    libreria = Libreria()
    libreria.agregar_libro("Cien años de soledad", "García Márquez", 30000)
    libreria.agregar_libro("El principito", "Saint-Exupéry", 10000)
    libreria.agregar_libro("Harry Potter", "Rowling", 50000)
    libreria.agregar_libro("Don Quijote", "Cervantes", 40000)

    print("--- Lista inicial ---")
    libreria.mostrar()

    libreria.marcar_vendido("Harry Potter")
    libreria.marcar_vendido("El principito")

    print(f"\n--- Recaudación: ${libreria.calcular_recaudacion():,} ---")

    print("\n--- Baratos (< $35000) no vendidos ---")
    baratos = libreria.obtener_baratos(35000)
    baratos.mostrar()

    print("\n--- Después de limpiar vendidos ---")
    libreria.limpiar_vendidos()
    libreria.mostrar()