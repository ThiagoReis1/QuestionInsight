from numpy import *

r = input(": ").upper()
custo = 0.12
custo1 = 0.18
i = 0
c = 0

while i < len(r):
	if (r[i] == "A" or r[i] == "E" or r[i] == "I" or r[i] == "O" or r[i] == "U"):
		c = c + custo
	elif (r[i] != "A" and r[i] != "E" and r[i] != "I" and r[i] != "O" and r[i] != "U"):
		c = c + custo1
	i = i + 1
	
print(round(c, 2))		
	
	
	
	
	
