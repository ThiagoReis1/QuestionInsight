from math import*

x=eval(input("Um angulo x, medido em radianos.: "))
k=int(input("Um número inteiro k, a quantidade de termos da série.: "))

coos=1.0
i=0

while(i < k):

	coos = coos - (((-1)**(i+1)) * (x**(i+1)/factorial(*2)))
	k=k-1
	
print(round(coos,6))