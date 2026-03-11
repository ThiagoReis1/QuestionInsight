from math import*
x = float(input())
k = int(input())
aux1 = 1
aux2 = 0
cont = 0
while (aux2 < k -1):
	cont += pow (x,aux1)/factorial(aux1)
	aux1 += 1
	aux2 +=1
cont += 1
print(round(cont,9))