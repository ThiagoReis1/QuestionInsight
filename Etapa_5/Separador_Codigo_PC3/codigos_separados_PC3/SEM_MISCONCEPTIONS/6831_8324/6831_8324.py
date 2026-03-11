from numpy import *
string = input("digite as respectivas letras para cada produto:").upper()
i = 0
total = 0
A = 0
L = 0
P = 0

while i < len(string):
	if string[i] == "A":
		total = total + 16.75
		A = A + 1
   elif string(i) == "L":
		total = total + 4,60
		L = L + 1
	elif string[i] == "P":
		total = total + 2.85
		P = P + 1
	i = i + 1
print(round(total,2), A, L, P)

	
		
		