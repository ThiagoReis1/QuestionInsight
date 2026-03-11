from numpy import*

vt = array(eval(input(":")))
f = 0
lista = []

for i in range(len(vt)):
	if(vt[i] >= 2000):
		f += 1
		lista.append(i)
print(f)
print(array(lista))
