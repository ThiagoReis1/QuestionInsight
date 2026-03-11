from math import*
dias = int(input("Digite quantos dias ficou hospedado?: "))
diaria = 175.0
x = dias * diaria
if dias < 15:
	valor = x + 20.0
if dias == 15:
	valor = x + 16.0
if dias > 15:
	valor = x + 10.0
print(valor)
