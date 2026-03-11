from numpy import *
cor = (input("Informe a cor do olho do cliente: ").upper()).split(',')

a = 0
b = 0
c = 0
d = 0
e = 0

vet = zeros(5, dtype=int)

for i in range(0,len(cor)):
	if cor[i]=="P":
		a = a + 1
		vet[0] = a
	elif cor[i]=="C":
		b = b + 1
		vet[1] = b
	elif cor[i]=="M":
		c = c + 1
		vet[2] = c
	elif cor[i]=="V":
		d = d + 1
		vet[3] = d
	elif cor[i]=="A":
		e = e + 1
		vet[4] = e

print(max(vet))		
print(vet)
		
		
