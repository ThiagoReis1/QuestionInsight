from numpy import *
senha = input("senha: ")
custo = 0
for i in senha.upper():
	if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
		custo += 1.12
	else:
		custo += 1.18
print(round(custo, 2))