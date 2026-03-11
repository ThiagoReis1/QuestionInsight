from numpy import *

vet = array(eval(input("Insira: ")))
cont = 0

for i in range(size(vet)):
	if vet[i] >= 70:
		cont += 1
		
an = zeros(size(vet), dtype = int)
for i in range(size(an)):
	print(cont)
print(an)