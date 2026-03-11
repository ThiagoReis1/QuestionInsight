n=int(input("digite o numero de termos:"))
cont=1
sinal=-1
a=1
soma=0

while(cont<n+1):
	den=5+(2*a+1)
	soma=soma+sinal*cont**2/den
	sinal=-sinal
	a=a+1
	cont=cont+1
print(round(soma,10))