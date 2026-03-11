from numpy import*

e = input("abra: ")
i = 0
cont = 0
cont1 = 0
cont2 = 0
cont3 = 0

while i < len(e):
	if e[i] == "M":
		cont = cont + 7.25
		cont1 = cont1 + 1
	if e[i] == "P":
		cont = cont + 4.75
		cont2 = cont2 + 1
	if e[i] == "R":
		cont = cont + 3.50
		cont3 = cont3
	i += 1
	
print(round(cont, 2))