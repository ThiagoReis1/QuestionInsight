from math import *

n = int(input("ano de nascimento"))
pais =  input("Brasil ou Japao? ").upper()
idade = 2023 - n

if idade>=21 and pais == "B" or idade >=20 and pais == "J":
	print("sim")
	if pais == "B":
		print(abs(21-idade))
	else:
		print(abs(20-idade))
elif idade<21 and pais == "B" or idade<20 and pais == "J":
	print("nao")
	if pais == "B":
		print(abs(21-idade))
	else:
		print(abs(20-idade))
else:
	print("invalido")