from math import*
x = float(input("Digite:"))
k = int(input("Digite:"))
cosh = 1 
cont = 2
variavel = 2
while(cont <= k):
	cosh = cosh + ((x**variavel)/factorial(variavel))
	variavel = variavel + 2
	cont = cont + 1
print(round(cosh,8))