from numpy import*

vs = array(eval(input("Valor: ")))
vac = 0 

for i in range (size(vs)):
	if (vs[i] <= 50):
		vac += 1
print(vac)

a = zeros(vac, dtype = int)
h = 0

for i in range (size(vs)):
	if (vs[i] <= 50):
		a[h] = i
		h += 1
print(a)
	