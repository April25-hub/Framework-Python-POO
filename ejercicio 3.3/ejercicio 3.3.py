class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0: self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0: self.cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0, edad=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad

    def esTitularValido(self):
        return 18 <= self.edad < 25

    def mostrar(self):
        print(f"Cuenta Joven - Titular: {self.titular}, Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion}%")

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para retirar dinero.")


# Ejemplo de uso
cuenta_carlos = CuentaJoven("Carlos", 500, 5, 22)
cuenta_carlos.mostrar()  # Mostrar datos
cuenta_carlos.retirar(100)  # Retirar dinero
cuenta_carlos.mostrar()  # Mostrar saldo después del retiro

cuenta_maria = CuentaJoven("María", 800, 3, 30)
cuenta_maria.retirar(50)  # Intentar retirar dinero (no es titular válido)
