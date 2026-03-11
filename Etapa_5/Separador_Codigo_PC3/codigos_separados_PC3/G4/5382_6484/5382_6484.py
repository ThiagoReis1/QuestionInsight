from numpy import*

v = input("").upper()
a = 0
b = 0
cont = 0

while a < len(v):
	if v[a] == "A" or v[a] == "E" or v[a] == "I" or v[a] == "O" or v[a] == "U":
		cont = cont + 0.25
	else:
		b = b + 0.27
	a = a + 1
total = cont + b
print(round(total,2))
			 
			 