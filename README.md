# Framework-Python-POO
# 1
Arzaba Diaz April 1173 3W
![image](https://github.com/user-attachments/assets/1cda3ad8-a6ba-4db8-92ca-ed56fb35ddb2)
![image](https://github.com/user-attachments/assets/864e7a71-4ae6-4e1f-8f05-b24326c6d87c)
# 2
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        """
        Constructor de la clase Cuenta.

        :param titular: Nombre del titular de la cuenta (obligatorio).
        :param cantidad: Cantidad inicial en la cuenta (opcional, por defecto 0.0).
        """
        self.__titular = titular
        self.__cantidad = cantidad

    # Getters
    def get_titular(self):
        """
        Obtiene el titular de la cuenta.
        """
        return self.__titular

    def get_cantidad(self):
        """
        Obtiene la cantidad actual en la cuenta.
        """
        return self.__cantidad

    # Setters (controlados mediante métodos ingresar y retirar)
    def ingresar(self, cantidad):
        """
        Ingresa una cantidad a la cuenta. Si la cantidad es negativa, no hace nada.

        :param cantidad: Monto a ingresar.
        """
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta. La cuenta puede quedar en números rojos.

        :param cantidad: Monto a retirar.
        """
        self.__cantidad -= cantidad

    # Metodo para mostrar los datos
    def mostrar(self):
        """
        Muestra los datos de la cuenta.
        """
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")
