from abc import ABC, abstractmethod
from datetime import date

class CuentaBancaria(ABC):
    def __init__(self, nro_cuenta, cbu, alias, saldo):
        self._nro_cuenta = nro_cuenta
        self._cbu = cbu
        self._alias = alias
        self._saldo = saldo
        self._movimientos = []

    @property
    def nro_cuenta(self):
        return self._nro_cuenta

    @property
    def cbu(self):
        return self._cbu

    @property
    def alias(self):
        return self._alias

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    @property
    def movimientos(self):
        return self._movimientos

    def consultar_saldo(self):
        return self._saldo

    def depositar(self, monto_a_depositar):
        if monto_a_depositar > 0:
            self._saldo += monto_a_depositar
            self._movimientos.append((date.today(), "depósito", monto_a_depositar, self._saldo))
            return True
        return False

    @abstractmethod
    def extraer(self, monto_a_extraer):
        pass

    @abstractmethod
    def transferir(self, monto_a_transferir, cuenta_destino):
        pass

# esta clase hereda de CuentaBancaria
class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_limite_extracciones, monto_limite_transferencias, cant_extracciones_disponibles, cant_transferencias_disponibles):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self._monto_limite_extracciones = monto_limite_extracciones
        self._monto_limite_transferencias = monto_limite_transferencias
        self._cant_extracciones_disponibles = cant_extracciones_disponibles
        self._cant_transferencias_disponibles = cant_transferencias_disponibles

    def extraer(self, monto_a_extraer):
        if (monto_a_extraer > 0 and 
            monto_a_extraer <= self._saldo and 
            monto_a_extraer <= self._monto_limite_extracciones and 
            self._cant_extracciones_disponibles > 0):
            self._saldo -= monto_a_extraer
            self._cant_extracciones_disponibles -= 1
            self._movimientos.append((date.today(), "extracción", monto_a_extraer, self._saldo))
            return True
        return False

    def transferir(self, monto_a_transferir, cuenta_destino):
        if (monto_a_transferir > 0 and 
            monto_a_transferir <= self._saldo and 
            monto_a_transferir <= self._monto_limite_transferencias and 
            self._cant_transferencias_disponibles > 0):
            self._saldo -= monto_a_transferir
            cuenta_destino.saldo += monto_a_transferir
            self._cant_transferencias_disponibles -= 1
            self._movimientos.append((date.today(), "transferencia", monto_a_transferir, self._saldo))
            return True
        return False

# lo mismo
class CuentaCorriente(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_maximo_descubierto):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self._monto_maximo_descubierto = monto_maximo_descubierto

    def extraer(self, monto_a_extraer):
        if monto_a_extraer > 0 and monto_a_extraer <= self._saldo + self._monto_maximo_descubierto:
            self._saldo -= monto_a_extraer
            self._movimientos.append((date.today(), "extracción", monto_a_extraer, self._saldo))
            return True
        return False

    def transferir(self, monto_a_transferir, cuenta_destino):
        if monto_a_transferir > 0 and monto_a_transferir <= self._saldo + self._monto_maximo_descubierto:
            self._saldo -= monto_a_transferir
            cuenta_destino.saldo += monto_a_transferir
            self._movimientos.append((date.today(), "transferencia", monto_a_transferir, self._saldo))
            return True
        return False


class Cliente:
    def __init__(self, razon_social, cuit, tipo_persona, domicilio):
        self._razon_social = razon_social
        self._cuit = cuit
        self._tipo_persona = tipo_persona
        self._domicilio = domicilio
        self._cuentas_bancarias = []

    @property
    def razon_social(self):
        return self._razon_social

    @property
    def cuentas_bancarias(self):
        return self._cuentas_bancarias

    def crear_nueva_cuenta_bancaria(self, cuenta):
        self._cuentas_bancarias.append(cuenta)
        return True


class Banco:
    def __init__(self, nombre, domicilio):
        self._nombre = nombre
        self._domicilio = domicilio
        self._clientes = []

    @property
    def clientes(self):
        return self._clientes

    def crear_nuevo_cliente(self, cliente):
        self._clientes.append(cliente)
        return True

def main():
    banco = Banco("Banco Central", "Morat 123")

    # clientes
    cliente1 = Cliente("Lola Rodriguez", "20-12345678-9", "física", "Calle A")
    cliente2 = Cliente("Ludovico Commenge", "30-98765432-1", "jurídica", "Calle B")
    cliente3 = Cliente("Olivia Rodrigo", "27-11223344-8", "física", "Calle C")

    # cliente 1
    caja_ahorro1 = CajaDeAhorro("123", "0001", "CajaAhorroLola", 1000.0, 500.0, 2000.0, 5, 5)
    cuenta_corriente1 = CuentaCorriente("456", "0002", "CtaCteLola", 2000.0, 1000.0)
    cliente1.crear_nueva_cuenta_bancaria(caja_ahorro1)
    cliente1.crear_nueva_cuenta_bancaria(cuenta_corriente1)

    # cliente 2
    caja_ahorro2 = CajaDeAhorro("789", "0003", "CajaAhorroLudovico", 3000.0, 1000.0, 5000.0, 10, 10)
    cuenta_corriente2 = CuentaCorriente("101", "0004", "CtaCteLudovico", 4000.0, 2000.0)
    cliente2.crear_nueva_cuenta_bancaria(caja_ahorro2)
    cliente2.crear_nueva_cuenta_bancaria(cuenta_corriente2)

    # cliente 3
    caja_ahorro3 = CajaDeAhorro("112", "0005", "CajaAhorroOlivia", 1500.0, 700.0, 2500.0, 7, 7)
    cuenta_corriente3 = CuentaCorriente("113", "0006", "CtaCteOlivia", 3500.0, 1500.0)
    cliente3.crear_nueva_cuenta_bancaria(caja_ahorro3)
    cliente3.crear_nueva_cuenta_bancaria(cuenta_corriente3)

    # agrego clientes
    banco.crear_nuevo_cliente(cliente1)
    banco.crear_nuevo_cliente(cliente2)
    banco.crear_nuevo_cliente(cliente3)

    # simulacion de operaciones
    caja_ahorro1.depositar(550)
    cuenta_corriente2.extraer(700)
    caja_ahorro3.transferir(100, cuenta_corriente1)

    # info de los clientes
    for cliente in banco.clientes:
        print(f"Cliente: {cliente.razon_social}")
        for cuenta in cliente.cuentas_bancarias:
            print(f"  Tipo de cuenta: {type(cuenta).__name__}")
            print(f"  Saldo: {cuenta.consultar_saldo()}")
            print(f"  Movimientos: {cuenta.movimientos}")
        print("\n")

if __name__ == "__main__":
    main()