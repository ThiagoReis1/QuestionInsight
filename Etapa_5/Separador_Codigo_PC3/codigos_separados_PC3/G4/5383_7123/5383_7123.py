from numpy import*

v = input("digite o rotulo:").upper()

i = 0
c = 0

while i < len(v) :
	if (v[i] == "A" or v[i] == "E" or v[i] == "I" or v[i] == "O" or v[i] == "U") : 
		c = c + 0.12
	else:
		c = c + 0.18
	i = i + 1
	
print(round(c, 2))