from numpy import *
vet = array(eval(input("vet? ")))
soma =  zeros(size(vet), dtype = float)
n = 0
for i in range(size(vet)):
	if vet[i] > 170:
		soma[i] = vet[i]
		n += 1
	elif vet[i] < 170:
		soma[i] = 0

if sum(soma) == 0:
	print(0.0)
else:
	somaf = sum(soma) / n
	print(round(somaf, 2))

	