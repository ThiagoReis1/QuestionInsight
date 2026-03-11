from math import*
angulo=radians(eval(input("angulo:")))
numero=int(input("termos de serie:"))

cont=0
soma=0

while(angulo >= 0):
	f = (((1) ** cont)) *(angulo ** (1 * cont + 1))/(factorial(2 * cont + 1))
	soma = soma + f
	cont = cont + 1
	print(round(f,6))
	