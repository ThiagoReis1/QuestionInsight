# Função F.

x = float(input("Digite o valor:"))

if((x<=(-1))or(x>=1)):
	f=(2*x)
elif((-1<x<0)or(0<x<1)):
	f=(2*x)
else:
	f=(*x)
print(round(f,2))