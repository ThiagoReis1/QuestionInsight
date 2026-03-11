from numpy import*

x = array(eval(input(": ")))

cont = 0

while cont < size(x):
	if x[cont] > 8:
		x[cont] = 10
	if x[cont] < 2:
		x[cont] = 0
	cont = cont + 1
print(x)
