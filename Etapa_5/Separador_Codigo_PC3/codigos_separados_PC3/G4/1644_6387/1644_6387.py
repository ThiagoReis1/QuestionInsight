from numpy import *

notas = array(eval(input("Informe as notas: ")))
rp = 0 
ind = []

for i in range(size(notas)):
	if notas[i] < 5:
		rp = rp + 1
		ind.append(i)
u = zeros(size(ind),dtype=int)
u = u + ind
print(rp)
print(u)