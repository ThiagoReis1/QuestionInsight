from numpy import * 
s = input("Ler a string: ") 

i = 0
total = 0

M = 0
P = 0
R = 0

while i < len(s):
	if s[i] == "M":
		total = total + 7.25
		M = M+1	
	elif s[i] == "P":
		total = total + 4.75
		P = P + 1
	elif s[i] == "R":
		R = R + 1
		total = total + 3.50
	i = i + 1
	
print(round(total, 2), M, P, R)