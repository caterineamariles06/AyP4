
class Cancion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        self.siguiente = None
        self.anterior = None
    
    def duracion_formato(self):
          # Convierte la duración total (en segundos) a minutos
        minutos = self.duracion// 60
        
    # Obtiene los segundos restantes
        segundos = self.duracion % 60
        
    # Retorna la duración en minutos y segundos
        return f"{minutos}:{segundos:02d}"



class Reproductor:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None
        
    def esta_vacia(self):
        #Verifica si la lista esta vacia
        return self.cabeza is None  #retorna un booleano

    
    """def insertar_inicio(self, nombre, duracion):
        nuevo = Cancion(nombre, duracion)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo"""


    def insertar_final(self, nombre, duracion):
        nuevo = Cancion(nombre, duracion)

        # Caso lista vacía
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            self.actual = nuevo
            print("Canción agregada")
            return

        # Llamada recursiva desde la cabeza
        self._insertar_final_recursivo(self.cabeza, nuevo)
        print("Canción agregada")

    def _insertar_final_recursivo(self, nodo, nuevo):
        # Caso base: llegamos al último nodo
        if nodo.siguiente is None:
            nodo.siguiente = nuevo
            nuevo.anterior = nodo
            self.cola = nuevo
            return

        # Llamada recursiva
        self._insertar_final_recursivo(nodo.siguiente, nuevo)

    # Mostrar lista de canciones
    """def mostrar_lista(self):
        if self.esta_vacia():
            print("Lista vacia")
            return
        actual = self.cabeza
        print("\n Lista de canciones:")
        while actual:
            if actual == self.actual:
                print(f" {actual.nombre} ({actual.duracion_formato()})  <-- Reproduciendo")
            else:
                print(f"  {actual.nombre} ({actual.duracion_formato()})")

            actual = actual.siguiente"""
    def mostrar_lista(self):
        if self.esta_vacia():
            print("Lista vacía")
            return

        print("\nLista de canciones:")
        self._mostrar_recursivo(self.cabeza)

    
    def _mostrar_recursivo(self, actual):
            # Caso base: no hay más nodos
            if actual is None:
                return

            # Mostrar el actual actual
            if actual == self.actual:
                print(f" {actual.nombre} ({actual.duracion_formato()})  <-- Reproduciendo")
            else:
                print(f"  {actual.nombre} ({actual.duracion_formato()})")

            # Llamada recursiva al siguiente actual
            self._mostrar_recursivo(actual.siguiente)


      

    # Reproducir canción actual
    def reproducir(self):
        if self.actual:
            print(f"Reproduciendo: {self.actual.nombre} ({self.actual.duracion_formato()})")
        else:
            print("No hay canciones")

    # Pasar a la siguiente canción
    def siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            self.reproducir()
        else:
            print("No hay siguiente canción")

    # Volver a la canción anterior
    def anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            self.reproducir()
        else:
            print(" No hay canción anterior")

    # Eliminar una canción por nombre
    def _eliminar_recursivo(self, actual, nombre):

        # ===============================
        # CASO BASE 1: No se encontró
        # ===============================
        # Si actual es None significa que llegamos al final de la lista
        # y no encontramos la canción
        if actual is None:
            print("Canción no encontrada")
            return   # Se detiene la recursión


        # ===============================
        # CASO: Encontramos la canción
        # ===============================
        # Si el nombre del nodo actual coincide con el nombre buscado
        if actual.nombre == nombre:

            # ---------------------------------
            # CASO 1: Es la primera canción (cabeza)
            # ---------------------------------
            # Si no tiene nodo anterior, significa que es la cabeza
            if actual.anterior is None:

                # La cabeza ahora será el siguiente nodo
                self.cabeza = actual.siguiente

                # Si existe un nuevo nodo cabeza
                if self.cabeza:
                    # Se elimina el enlace hacia atrás
                    self.cabeza.anterior = None
                else:
                    # Si no existe, significa que la lista quedó vacía
                    self.cola = None


            # ---------------------------------
            # CASO 2: No es la primera
            # ---------------------------------
            else:
                # El nodo anterior debe saltarse el nodo actual
                # y apuntar al siguiente
                actual.anterior.siguiente = actual.siguiente


            # ---------------------------------
            # CASO 3: No es la última
            # ---------------------------------
            if actual.siguiente:
                # El nodo siguiente debe apuntar hacia atrás
                # al nodo anterior del eliminado
                actual.siguiente.anterior = actual.anterior
            else:
                # Si no hay siguiente, era la última (cola)
                # Entonces actualizamos la cola
                self.cola = actual.anterior


            # ---------------------------------
            # Ajustar la canción actual
            # ---------------------------------
            # Si la canción que estamos eliminando
            # es la que se estaba reproduciendo
            if self.actual == actual:

                # Si hay siguiente canción, reproducirá esa
                if actual.siguiente:
                    self.actual = actual.siguiente
                else:
                    # Si no hay siguiente, pasa a la anterior
                    self.actual = actual.anterior


            print("Canción eliminada")
            return   # Detiene la recursión porque ya eliminó


        # ===============================
        # CASO RECURSIVO
        # ===============================
        # Si no es la canción buscada,
        # llama al método con el siguiente nodo
        self._eliminar_recursivo(actual.siguiente, nombre)


def menu():
    print("\nREPRODUCTOR DE CANCIONES ")
    print("1. Agregar canción")
    print("2. Mostrar lista")
    print("3. Reproducir canción actual")
    print("4. Siguiente canción")
    print("5. Canción anterior")
    print("6. Eliminar canción")
    print("7. Salir")



reproductor = Reproductor()

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la canción: ")
        duracion = int(input("Duracion de la canción: "))

        reproductor.insertar_final(nombre, duracion)

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
        print(" Opción inválida")
