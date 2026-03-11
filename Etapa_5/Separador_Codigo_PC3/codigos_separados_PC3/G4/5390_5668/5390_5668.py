from numpy import *
e = array(input("rotulo da etiqueta: ").upper())
c = zeros(size(e))
i = 0
v = array(['A', 'E', 'I', 'O', 'U'])
while i < size(e):
	if e[:i] == v[:i]:
		c[i] = 0.19
	else:
		c[i] = 0.23
ct = sum(c)
print(round(ct, 2))