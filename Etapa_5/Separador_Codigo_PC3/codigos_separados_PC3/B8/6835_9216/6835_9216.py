from numpy import *

string = input("Digite: ").upper()
i = 0
b = 0
c = 0
e = 0

while (i < len(string)):
	if (string[i] == 'B'):
		b = b + 1
	elif (string[i] == 'C'):
		c = c + 1
	elif (string[i] == 'E'):
		e = e + 1
	
	i = i + 1

compra = (b * 3.75) + (c * 7.90) + (e * 9.85)

print (round(compra,2))