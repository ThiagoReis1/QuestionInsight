from numpy import*
string = input("digite: ")
i = 0
p1,p2,p3 = 0,0,0
acogue = 0
laticinios = 0
padaria = 0 

while (i < len(string)):
	if (string[i] == "A"):
		acogue = acogue + 19.90
		p1 = p1 + 1
	if (string[i] == "L"):
		laticinios = laticinios + 3.50
		p2 = p2 + 1
	if(string[i] == "P"):
		padaria = padaria + 4.25
		p3 = p3 + 1
	i += 1
print(round(acogue + laticinios + padaria, 2))