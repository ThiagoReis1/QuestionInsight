from numpy import *

letra = input("").upper()

i = 0 
b = 0

while i < len(letra):
	if letra[i] == "B":
		b = b + 1
		
	i = i + 1

print(b)