from datetime import date
from math import pi

""" formas de concatenar
print("hola" + " " + "mundo")
Esta primera manera de concatenar no 
sirve para concatenar variables
hola = "hola"
mundo = "mundo"
print(hola,mundo) """

min = (1.35 * 100) - 40
""" min = (1 * 60) + 35 """
print(min)
print(type(min))

# _____________________________________

""" 1. Sumar 3 números y mostrar su resultado """

n1 = float(input("Ingrese el número 1: "))
n2 = float(input("Ingrese el número 2: "))
n3 = float(input("Ingrese el número 3: "))
s = n1 + n2 + n3 

print(s)
print(type(s))

""" 2. Restar 2 números y mostrar su resultado """

n1 = float(input("Ingrese el número 1: "))
n2 = float(input("Ingrese el número 2: "))
r = n1 - n2 

print(r)
print(type(r))

""" 3. Multiplicar 3 números y mostrar su resultado """

n1 = float(input("Ingrese el número 1: "))
n2 = float(input("Ingrese el número 2: "))
n3 = float(input("Ingrese el número 3: "))
m = n1 * n2 * n3

print(m)
print(type(m))

""" 4. Dividir 2 números y mostrar su resultado """

n1 = float(input("Ingrese el número 1: "))
n2 = float(input("Ingrese el número 2: "))
d = n1 / n2 

print(d)
print(n1 / n2)
print(type(d))

""" 5. Dividir 2 números y mostrar su resultado """

n1 = float(input("Ingrese el número 1: "))
n2 = float(input("Ingrese el número 2: "))
d = n1 / n2 

print(d)
print(type(d))

""" 6. Conociendo el año de nacimiento de una persona, calcular su edad actual """

naci = float(input("Ingrese el año de nacimiento: "))
actual = float(format(date.today().year))
edad = actual - naci
print(edad)
print(type(edad))
""" 
today = date.today()

print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))

 """

""" numero = 11 
print(numero, id(numero)) """


# Área de figuras geométricas

""" cuadrado """
lado = float(input("Ingrese el lado: "))
area = lado**2
perimetro = lado*4

print("El área del cuadrado es: ", area,"\nEl perímetro del cuadrado es: ", perimetro)


""" rectangulo """
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area = base*altura
perimetro = base*2 + altura*2

print("El área del resctangulo es: ", area,"\nEl perímetro del rectangulo es: ", perimetro)


""" triángulo solo si es equilátero"""
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area = base * altura / 2
perimetro = base*3

print("El área del triángulo es: ", area,"\nEl perímetro del triángulo es: ", perimetro)


""" rombo si es equilátero"""
diagonal_mayor = float(input("Ingrese la diagonal mayor: "))
diagonal_menor = float(input("Ingrese la diagonal menor: "))
lado = float(input("Ingrese el lado: "))
area = diagonal_mayor * diagonal_menor / 2
perimetro = lado*3

print("El área del rombo es: ", area,"\nEl perímetro del rombo es: ", perimetro)


""" romboide si tiene 2a + 2b de perimetro """
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
lado = float(input("Ingrese el lado: "))
area = diagonal_mayor * diagonal_menor / 2
perimetro = lado*3

print("El área del romboide es: ", area,"\nEl perímetro del romboide es: ", perimetro)


""" trapecio solo si es isósceles """
base_mayor = float(input("Ingrese la base mayor: "))
base_menor = float(input("Ingrese la base menor: "))
altura = float(input("Ingrese la altura: "))
lado = float(input("Ingrese el lado: "))
area = altura * (base_mayor * base_menor) / 2
perimetro = lado*2 + base_menor + base_mayor

print("El área del trapecio es: ", area,"\nEl perímetro del trapecio es: ", perimetro)


""" circulo """
radio = float(input("Ingrese el radio: "))
area = pi * (radio**2)
perimetro = pi * radio * 2

print("El área del circulo es: ", area,"\nEl perímetro del circulo es: ", perimetro)


""" Polígonos si son regulares """
apotema = float(input("Ingrese la apotema: "))
lado = float(input("Ingrese el lado: "))
numero_lados = float(input("Ingrese el número de lados: "))
area = numero_lados * apotema * lado / 2 
perimetro = numero_lados * lado

print("El área del circulo es: ", area,"\nEl perímetro del circulo es: ", perimetro)



