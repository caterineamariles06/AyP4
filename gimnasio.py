class Miembro:
    def __init__(self, nombre, edad, mensualidad):
        self.nombre = nombre
        self.edad = edad
        self.activo = True             # ✅ nacen activos
        self.mensualidad = mensualidad
        self.siguiente = None
        self.anterior = None

class Gimnasio:
    def __init__(self):
        self.inicio = None

    def agregar(self, nombre, edad, mensualidad):
        nuevo = Miembro(nombre, edad, mensualidad)   # ✅ Miembro, no NodoDoble
        if self.inicio is None or self.inicio.mensualidad < nuevo.mensualidad:
            nuevo.siguiente = self.inicio
            if self.inicio:
                self.inicio.anterior = nuevo
            self.inicio = nuevo
        else:
            self._agregar_rec(self.inicio, nuevo)

    def _agregar_rec(self, nodo, nuevo):
        if nodo.siguiente is None or nodo.siguiente.mensualidad < nuevo.mensualidad:
            nuevo.siguiente = nodo.siguiente
            nuevo.anterior = nodo
            if nodo.siguiente:
                nodo.siguiente.anterior = nuevo
            nodo.siguiente = nuevo
        else:
            self._agregar_rec(nodo.siguiente, nuevo)

    def contar_activos_mayores(self, minimo):
        return self._contar_activos_mayores(self.inicio, minimo)

    def _contar_activos_mayores(self, nodo, minimo):
        if nodo is None:
            return 0
        cont = 1 if nodo.edad > minimo and nodo.activo else 0  # ✅ verifica activo
        return cont + self._contar_activos_mayores(nodo.siguiente, minimo)  # ✅ pasa minimo

    def obtener_premium(self, minimo):
        nueva_lista = Gimnasio()
        return self._obtener_premium_rec(self.inicio, nueva_lista, minimo)

    def _obtener_premium_rec(self, nodo, lista, minimo):
        if nodo is None:
            return lista
        if nodo.mensualidad > minimo and nodo.activo:   # ✅ mensualidad
            lista.agregar(nodo.nombre, nodo.edad, nodo.mensualidad)
        return self._obtener_premium_rec(nodo.siguiente, lista, minimo)

    def limpiar_inactivos(self):
        self.inicio = self._limpiar_rec(self.inicio)
        if self.inicio:
            self.inicio.anterior = None

    def _limpiar_rec(self, nodo):
        if nodo is None:
            return None
        if not nodo.activo:
            return self._limpiar_rec(nodo.siguiente)
        nodo.siguiente = self._limpiar_rec(nodo.siguiente)
        if nodo.siguiente:
            nodo.siguiente.anterior = nodo
        return nodo

    def desactivar(self, nombre):
        actual = self.inicio
        while actual:
            if actual.nombre == nombre:
                actual.activo = False
                return
            actual = actual.siguiente

    def mostrar(self):
        actual = self.inicio
        if actual is None:
            print("Gimnasio vacío")
            return
        while actual:
            estado = "✓" if actual.activo else "○"
            print(f"[{estado}] {actual.nombre} | {actual.edad} años | ${actual.mensualidad:,}")
            actual = actual.siguiente


if __name__ == "__main__":
    print("=" * 50)
    print("           PRUEBAS GIMNASIO")
    print("=" * 50)

    g = Gimnasio()
    g.agregar("Carlos", 35, 200000)
    g.agregar("Ana", 25, 50000)
    g.agregar("Luis", 40, 150000)
    g.agregar("Maria", 28, 100000)

    print("\n--- Lista inicial ---")
    g.mostrar()
    # Esperado: Carlos(200000) > Luis(150000) > Maria(100000) > Ana(50000)

    print(f"\n--- Activos mayores de 30 años: {g.contar_activos_mayores(30)} ---")
    # Esperado: 2 (Carlos 35, Luis 40)

    print("\n--- Premium (> $100000) activos ---")
    premium = g.obtener_premium(100000)
    premium.mostrar()
    # Esperado: Carlos y Luis

    g.desactivar("Carlos")
    g.desactivar("Ana")

    print("\n--- Después de limpiar inactivos ---")
    g.limpiar_inactivos()
    g.mostrar()
    # Esperado: Luis y Maria