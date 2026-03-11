from numpy import*

n= input("insira o produto:").upper()
total= 0
C= 0
E= 0
P= 0
i=0
while i < len(n):
	if n[i]== "C":
		total+= 10.5
		C+=1
	if n[i]== "E":
		total += 8.75
		E+= 1
	if n[i] == "P":
		total += 17.90
		P+=1
	i+=1

print(round(total,2),C,E,P)
