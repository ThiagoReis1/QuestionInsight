x=float(input("digite um numero"))
k=int(input("digite um numero"))
cont=0
soma=2

while(-1<x<1):
	if(k==1):
		cont=1-(x**soma)
	else:
		soma=soma+2
		cont=x**soma
		cont1=-x**soma
		cont=cont+cont1
		k=int(input("digite um numero"))
	print(cont)
		
	