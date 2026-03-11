from numpy import *
al = array(eval(input()))
imp = 0
for i in al:
	if i % 2 != 0:
		imp = imp + 1
print(imp)
vet_impar = zeros(imp, dtype=int)
i=0
for cont in range(0, size(al)):
	if al[cont] % 2 != 0:
		vet_impar[i]=cont
		i=i+1
print(vet_impar)