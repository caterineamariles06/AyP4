# =========================
# CLASE NODO (CANCIÓN)
# =========================
class Cancion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None


# =========================
# CLASE REPRODUCTOR CIRCULAR
# =========================
class ReproductorCircular:
    def __init__(self):
        self.actual = None  # Apunta a la canción actual

    # Agregar canción
    def agregar_cancion(self, nombre):
        nueva = Cancion(nombre)

        # Lista vacía
        if self.actual is None:
            nueva.siguiente = nueva
            nueva.anterior = nueva
            self.actual = nueva
        else:
            ultima = self.actual.anterior

            ultima.siguiente = nueva
            nueva.anterior = ultima
            nueva.siguiente = self.actual
            self.actual.anterior = nueva

        print(" Canción agregada")

    # Mostrar lista de canciones
    def mostrar_lista(self):
        if self.actual is None:
            print("No hay canciones")
            return

        print("\n🎶 Lista de canciones:")
        temp = self.actual

        while True:
            if temp == self.actual:
                print("▶", temp.nombre)
            else:
                print(" -", temp.nombre)

            temp = temp.siguiente
            if temp == self.actual:
                break

    # Reproducir canción actual
    def reproducir(self):
        if self.actual:
            print("▶ Reproduciendo:", self.actual.nombre)
        else:
            print(" No hay canciones")

    # Siguiente canción (nunca se acaba)
    def siguiente(self):
        if self.actual:
            self.actual = self.actual.siguiente
            self.reproducir()
        else:
            print(" No hay canciones")

    # Canción anterior (nunca se acaba)
    def anterior(self):
        if self.actual:
            self.actual = self.actual.anterior
            self.reproducir()
        else:
            print(" No hay canciones")

    # Eliminar canción por nombre
    def eliminar_cancion(self, nombre):
        if self.actual is None:
            print(" Lista vacía")
            return

        temp = self.actual

        while True:
            if temp.nombre == nombre:
                # Si es la única canción
                if temp.siguiente == temp:
                    self.actual = None
                else:
                    temp.anterior.siguiente = temp.siguiente
                    temp.siguiente.anterior = temp.anterior

                    if self.actual == temp:
                        self.actual = temp.siguiente

                print("🗑 Canción eliminada")
                return

            temp = temp.siguiente
            if temp == self.actual:
                break

        print(" Canción no encontrada")


# =========================
# MENÚ INTERACTIVO
# =========================
def menu():
    print("\n REPRODUCTOR DE CANCIONES (CIRCULAR) ")
    print("1. Agregar canción")
    print("2. Mostrar lista")
    print("3. Reproducir canción actual")
    print("4. Siguiente canción")
    print("5. Canción anterior")
    print("6. Eliminar canción")
    print("7. Salir")


# =========================
# PROGRAMA PRINCIPAL
# =========================
reproductor = ReproductorCircular()

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la canción: ")
        reproductor.agregar_cancion(nombre)

    elif opcion == "2":
        reproductor.mostrar_lista()

    elif opcion == "3":
        reproductor.reproducir()

    elif opcion == "4":
        reproductor.siguiente()

    elif opcion == "5":
        reproductor.anterior()

    elif opcion == "6":
        nombre = input("Nombre de la canción a eliminar: ")
        reproductor.eliminar_cancion(nombre)

    elif opcion == "7":
        print("Saliendo del reproductor...")
        break

    else:
        print("Opción inválida")
