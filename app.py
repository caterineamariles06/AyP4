class Estudiante:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
    
estudiante1=Estudiante("Pepito",12345)
print(estudiante1.nombre)
