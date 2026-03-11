from math import* 
n= (int(input("Digite o valor: ")))
i= 0
cont=3
soma= 0
sinal= -i
while i<=n:
	soma = soma+(sqrt(i)/cont+4)
	cont=cont+2
	i= i+sinal
print(round(soma,9))