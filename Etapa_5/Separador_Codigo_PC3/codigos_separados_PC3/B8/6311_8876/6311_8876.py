from numpy import *

string = input("").upper()

congelados = 10.50
enlatados = 8.75
pescados = 17.90
total = 0

i = 0
c = 0
e = 0
p = 0

while i < len(string):
	if string[i] == "C":
		total = total + congelados
		c = c + 1
	elif string[i] == "E":
		total = total + enlatados
		e = e + 1
	elif string[i] == "P":
		total = total + pescados
		p = p + 1
	i = i + 1

print(round(total,2),c,e,p)
	
		
	