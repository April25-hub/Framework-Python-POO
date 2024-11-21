class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        # El constructor recibe titular y una cantidad opcional
        self.titular = titular
        self.cantidad = cantidad

    # Getter y setter para el titular
    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    # Getter y setter para la cantidad
    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    # Método mostrar que imprime los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")

    # Método para ingresar dinero en la cuenta
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se han ingresado {cantidad:.2f} a la cuenta.")
        else:
            print("No se puede ingresar una cantidad negativa.")

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
            print(f"Se han retirado {cantidad:.2f} de la cuenta.")
        else:
            print("No se puede retirar una cantidad negativa.")


# Ejemplo de uso:

# Crear una cuenta con titular "Juan" y cantidad inicial 1000
cuenta_juan = Cuenta("Juan", 1000)

# Mostrar los datos de la cuenta
cuenta_juan.mostrar()

# Ingresar dinero a la cuenta
cuenta_juan.ingresar(500)
cuenta_juan.mostrar()  # Debería mostrar 1500

# Retirar dinero de la cuenta
cuenta_juan.retirar(200)
cuenta_juan.mostrar()  # Debería mostrar 1300

# Intentar ingresar una cantidad negativa
cuenta_juan.ingresar(-100)  # No hará nada

# Intentar retirar una cantidad negativa
cuenta_juan.retirar(-50)  # No hará nada

# Mostrar el estado final de la cuenta
cuenta_juan.mostrar()
