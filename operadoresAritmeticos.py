from datetime import date
from datetime import datetime
from math import pi

""" Ejemplo de suma  """
num1 = 3
num2 = 4
suma = num1 + num2
print("suma: ", suma)
print(type(suma))

""" ejemplo de resta """
resta = num1 - num2
print("resta: ", resta)
print(type(resta))

""" ejemplo de multiplicación """
multiplicacion = num1 * num2
print("multiplicación: ", multiplicacion)
print(type(multiplicacion))

""" ejemplo de divición """
division = num1 / num2
print("división: ", division)
print(type(division))

""" ejemplo de residuo """
residuo = num1 % num2
print("residuo: ", residuo)
print(type(residuo))

""" ejemplo de devición con resultado entero """
divisionEntera = num1 // num2
print("division resultado entero: ", residuo)
print(type(divisionEntera))

""" ejemplo de potencia """
potencia = num1 ** num2
print("potencia es: ", potencia)
print(type(potencia))


""" ejemplo de una operación más grande """
resultado = 3 ** 3  * (13/5 * (2*4))
print("operacion: ", resultado)
print(type(resultado))


# _______________________________
actual = date.today()
print("El año actual es: ", actual)
print(type(actual))

actual = datetime.now()
print("El año actual es: ", actual)
print(type(actual))

print("pi: ", pi)
print(type(pi))

verdadero = True
print("Variable de valor verdadero: ", verdadero)
print(type(verdadero))

