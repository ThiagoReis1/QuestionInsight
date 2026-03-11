from numpy import*
N=array(eval(input("valor das compras")))
n=0#para acumular o total
p=0#para acumular a posicao do valor
l=0#acumular sem desconto
s=size(N)
while(p<s):
	if(N[p]>80):
		x=(N[p]-((N[p])*15)/100)
		n=n+x
	else:
		n=n+N[p]
	p=p+1
print(round(n,2))
