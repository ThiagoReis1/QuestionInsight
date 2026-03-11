from math import*

x = float(input())
k = int(input())
cont = 0
aux = 0


while(k >0 and cont < k):
	aux = aux + (pow(x,cont))/(factorial(cont))
	#aux = aux + 1
	cont = cont +1
	
print(round(aux,9))

	