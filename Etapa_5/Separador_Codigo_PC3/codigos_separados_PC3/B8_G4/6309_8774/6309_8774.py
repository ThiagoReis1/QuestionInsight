from numpy import *
vet = input().upper()

i= 0
h= 0
c= 0
l= 0
total = 0

while i < len(vet):
	if vet[i] == "H":
		total = total + 5.40
		h += 1
	elif vet[i] == "C":
		total= total + 8.95
		c +=1
	elif vet [i] == "L":
		total= total + 4.50
		l += 1
	i += 1
print(round(total, 2))
print(h, c, l)