from numpy import *
n = array(eval(input("").upper()))
b = array(eval(input("")))
i = 0
c = 0
while (i < size(n)):
	if (n[i] == "BANANA"):
		c = c + b[i] * 0.97
	elif (n[i] == "BIFE"):
		c = c + b[i] * 2.95
	elif (n[i] == "FEIJOADA"):
		c = c + b[i] * 1.27
	elif (n[i] == "OMELETE"):
		c = c + b[i] * 1.04
	elif (n[i] == "TOMATE"):
		c = c + b[i] * 0.2
	i = i + 1

print(round(c, 2))
		