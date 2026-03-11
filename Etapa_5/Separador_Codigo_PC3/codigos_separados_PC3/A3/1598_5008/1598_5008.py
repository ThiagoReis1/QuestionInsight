from numpy import *
custos = eval(input("custos: "))
c = 0
desc = 0
for i in custos:
	if (float(i) < 90):
		c += float(i)
	else:
		desc = float(i) - 6.5
		c += desc
print(round(c, 2))