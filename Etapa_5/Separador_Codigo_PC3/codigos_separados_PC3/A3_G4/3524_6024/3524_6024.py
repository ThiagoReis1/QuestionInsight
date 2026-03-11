from math import factorial
x = int(input("digite o numero: "))
k = int(input("digite a quant de termos: "))
cont = 0 
cosh = 0

while cont != k: 
	cosh = x**cont*2/factorial(cont*2)
	cont = cont + 1
print(round(cosh,8))