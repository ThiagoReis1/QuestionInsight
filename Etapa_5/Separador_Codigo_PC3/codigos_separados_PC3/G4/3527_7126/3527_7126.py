from math import*

x=float(input("digite a variavel x"))
k=int(input("digite a variavel k"))

cont=0
soma=0
acum=0
while(soma < k):
	acum = acum + x**cont/(factorial(cont))
	cont = cont + 1
	soma = soma + 1
	
print(round(acum,9))
	
	