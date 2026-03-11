from numpy import *

n = input(":").upper()
i = 0
p = 0

while i < len(n):
	if n[i] == "A" or n[i] == "E" or n[i]=="I" or n[i] == "O" or n[i] =="U":
		p = p + 0.19
		
	else:
		p = p + 0.23
		
	i = i + 1
	
print(round(p,2))