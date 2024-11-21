class Persona:
    def __init__(self, nombre='', edad=None, dni=''):
        self.nombre = nombre
        self.edad = edad if edad is not None else 0  #por defecto 0 si no se proporciona edad
        self.dni = dni

    #setters y getters con validaciones
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.nombre = nombre
        else:
            print("Nombre inválido. Debe ser una cadena no vacía.")

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            print("Edad inválida. Debe ser un número entero no negativo.")

    def get_edad(self):
        return self.edad

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.dni = dni
        else:
            print("DNI inválido. Debe ser una cadena de 9 caracteres.")

    def get_dni(self):
        return self.dni

    #metodo para mostrar los datos
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    #metodo para verificar si es mayor de edad
    def es_mayor_de_edad(self):
        return self.edad >= 18

#ejemplo de uso de la clase
persona = Persona('Juan Perez', 25, '12345678A')
persona.mostrar()  #muestra los datos de la persona
print("Es mayor de edad:", persona.es_mayor_de_edad())  #verifica si es mayor de edad
