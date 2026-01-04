class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # El doble guion bajo "__" hace que sea PRIVADO

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")

    def obtener_saldo(self): # Método público para ver el saldo protegido
        return self.__saldo

# Uso
cuenta = CuentaBancaria(100)
cuenta.depositar(50)
print(f"Saldo actual: {cuenta.obtener_saldo()}")