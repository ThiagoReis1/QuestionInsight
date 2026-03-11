from numpy import *
clientes = input("Clientes: ").upper()

i = 0

contp = 0
contc = 0
contr = 0
contl = 0
contb = 0
conti = 0

while (i < len(clientes)):
	if (clientes[i] == "P"):
		contp = contp + 1
		i = i + 1
	elif (clientes[i] == "C"):
		contc = contc + 1
		i = i + 1
	elif (clientes[i] == "R"):
		contr = contr + 1
		i = i + 1
	elif (clientes[i] == "L"):
		contl = contl + 1
		i = i + 1
	elif (clientes[i] == "B"):
		contb = contb + 1
		i = i + 1
	else:
		conti = conti + 1
		i = i + 1

total = array([contp, contc, contr, contl, contb])

print(max(total))
print(total)