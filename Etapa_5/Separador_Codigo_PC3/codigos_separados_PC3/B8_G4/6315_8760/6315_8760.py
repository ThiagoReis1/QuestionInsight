from numpy import *

prod = input("").upper()

i = 0
total = 0
I = 0
M = 0
S = 0
while i < len(prod):
	if prod[i] == "I":
		total = total + 3.75
		I = I + 1
		
	elif prod[i] == "M":
		total = total + 4.50
		M = M + 1
		
	elif prod[i] == "S":
		total = total + 2.90
		
		S = S + 1
	i = i + 1
	
print(round(total, 2), I, M, S)