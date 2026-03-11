from numpy import *
v = array(eval(input("Informe os pesos levantados: ")))
rec = 307
print(rec)
i = 0
n = 0
while(i < size(v)):
	if(v[i] < rec):
		n = n + 1
	i = i + 1

print(n)