from numpy import*

x = input("").upper()
B = 3.75
C = 7.90
E = 9.85
i = 0
temp = 0
cont = 0
b = 0
c = 0
e = 0
acum = 0

while i < len(x): 
	if x[i] == "B": 
		acum = acum + B
		b = b + 1
		
	if x[i] == "C":
		acum = acum + C
		c = c + 1
		
	if x[i] == "E":
		acum = acum + E
		e = e + 1
	i = i + 1
print(round(acum, 2), b, c, e)