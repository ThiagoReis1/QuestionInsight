from numpy import *

vet = array(eval(input("digite as turmas")))

imp = 0
a = 0

for a in range(size(vet)):
	if(vet[a] % 2 != 0):
		imp = imp + 1
impares = zeros(imp, dtype =int)

cont = -1
for a in range(size(vet)):
	if(vet[a] % 2 != 0):
		cont = cont + 1
		impares[cont] = a
print(imp)
print(impares)
		

