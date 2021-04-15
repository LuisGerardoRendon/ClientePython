# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport

from service.calculadora.calculadora import Client
from service.calculadora.ttypes import OperacionIvalida

if __name__ == "__main__":
    host = "localhost"
    port = 50000
    transport = TBufferedTransport(TSocket(host, port))
    protocol = TBinaryProtocol(transport)
    conexion = Client(protocol)

    transport.open()
    print(conexion.suma(3, 5))
    transport.close()

    bandera = True

    while bandera:
        print ("Escribe la operacion que deseas:  +, -, /, *")
        operacion = str(input())

        try:
            if operacion == "+":
                print("Escribe el numero 1: ")
                numero1 = int(input())
                print("Escribe el numero 2: ")
                numero2 = int(input())
                transport.open()
                resultado = conexion.suma(numero1, numero2);
                transport.close();
                print(f"El resultado de la suma es: {resultado} ")
            elif operacion == "-":
                print("Escribe el numero 1: ")
                numero1 = int(input())
                print("Escribe el numero 2: ")
                numero2 = int(input())
                transport.open()
                resultado = conexion.resta(numero1, numero2);
                transport.close();
                print(f"El resultado de la resta es: {resultado}")
            elif operacion == "*":
                print("Escribe el numero 1: ")
                numero1 = int(input())
                print("Escribe el numero 2: ")
                numero2 = int(input())
                transport.open()
                resultado = conexion.multiplicacion(numero1, numero2);
                transport.close();
                print(f"El resultado de la multiplicacion es: {resultado}" )
            elif operacion == "/":
                print("Escribe el dividendo")
                dividendo = int(input())
                print("Escribe el diviso")
                divisor = int(input())
                transport.open()
                resultado = conexion.division(dividendo, divisor)
                transport.close()
                print(f"El resultado de la division es:  {resultado}")
            else:
                print("Operacion invalida")
        except OperacionIvalida:
            print("Operacion invalida")
        finally:
            transport.close()




