c=float(input("valor da casa: "))
d=float(input("deposito inicial: "))
m=float(input("deposito mensal: "))
j=float(input("taxa de juros: "))

soma=d
i=1

if(c<=0 or d<=0 or m<=0 or j<=0):
	print("Dados incorretos")
else:
	while(c>soma):
		soma = round(soma,2) + m + (round(soma,2)+m)*(j/100)
		i = i +1
	print(i)
