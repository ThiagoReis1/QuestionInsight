from math import*
x=float(input("numero real:"))
k=int(input("termos da serie: "))

cont=0
soma=0
cima=1
baixo=2


while (cont<k):
	soma=soma +(x**cima)/factorial(baixo)
	cima=cima+2
	baixo=baixo+2
	cont=cont+1
print(round(soma, 6))