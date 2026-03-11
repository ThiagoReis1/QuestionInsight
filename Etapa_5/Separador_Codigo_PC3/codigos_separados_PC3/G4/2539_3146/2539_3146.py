from math import*

m=eval(input("Insira o angulo:"))
a=int(input("Numero de repeticoes:"))

cont=1
soma=1

while cont<a:
	y=(m**cont)/factorial(cont)
	soma=soma+y
	cont=cont+2
	
print(round(soma,10))


from math import *
x = eval(input("Insira o angulo:"))
k = int(input("Numero de repeticoes:"))
cont = 1
m = 0
soma = 0
while (cont>k):
	m = ((cont+1))*((x**soma)/(factorial(cont)))
	soma = soma + 1
	cont = cont + 1
print(round(m, 10))
