from numpy import * 
s = input("").upper()

a = 0
b = 0
x = 0

while a < len(s) :
	if s[a] == "A" or s[a] == "E" or s[a] == "I" or s[a] == "O" or s[a] == "U" :
		x = x + 3.15
	else:
		b = b + 4.17
	a = a + 1 
ct = x + b	
print(round(ct,2))