from numpy import *
produto = input("digite a sequencia")
total=0
i=0
m=0
p=0
r=0
# enquanto o indicie for menor que o tamanho 
while i < len(produto):
	if produto[i].upper() == "M":
		m += 7.25
		i+=1
	elif produto[i].upper() == "P":
		p+= 4.75
		i+=1
		
	elif produto[i].upper() == "R":
		r+= 3.50
		i+=1

total = m + p + r

print(round(total,2))