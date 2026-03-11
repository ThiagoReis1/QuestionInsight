from numpy import * 
p = input("Palavra: ").upper()
c = 0
i = 0
while i < len(p):
	if p[i] == "C":
		c = c + 1
	else:
		c = c + 0 
	i = i + 1
print(c)