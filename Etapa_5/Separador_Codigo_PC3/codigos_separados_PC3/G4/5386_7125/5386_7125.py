from numpy import*

x = input(": ").upper()

cont = 0 
y = 0

while cont < len(x):
	if x[cont] == "A" or x[cont] == "E" or x[cont] == "I" or x[cont] == "O" or x[cont] == "U":
		y = y + 1.12
	else:
		y = y + 1.18
	cont = cont + 1
print(round(y,2))