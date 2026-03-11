mi = float(input(""))

cont = 0
a = 0

while (mi >= 0.5):
	mi = mi - (mi * (10/100))
	cont = cont + 1
	a = a + 1
print(round(cont,2))