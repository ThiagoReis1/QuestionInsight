from math import*

x=float(input())
k=int(input())

cont=1
arctg=0
indice=1
termo=0
sinal=1

while k >= cont:
	termo=((x**indice)/(indice))
	arctg=arctg+(termo*sinal)
	cont=cont+1
	indice=indice+1
	sinal=sinal*(-1)
print(round(arctg,6))