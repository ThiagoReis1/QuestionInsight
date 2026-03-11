from math import*

x= float(input("Digite o numero: "))
k= int(input("Digite o numero: "))

c= 1
control = 2
variavel= 2

while (control <= k):
	c = c + ((x**variavel)/factorial(variavel))
	variavel = variavel + 2
	control= control + 1
print(round(c, 8))
