from numpy import *
crescente = True
v = eval(input("v: "))
for i in range(size(v)):
	if (i < size(v)-1):
		if (v[i+1] >= v[i]):
			crescente = True
		else:
			crescente = False
	else:
		if (v[i - 1] <= v[i]):
			crescente = True
		else:
			crescente = False
print(crescente)