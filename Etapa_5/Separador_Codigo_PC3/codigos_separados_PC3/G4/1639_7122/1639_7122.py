from numpy import*

vet = array(eval(input(": ")))

cont = 0

for i in range(0, size(vet)):
	if vet[i] % 2 == 0:
		cont = cont + 1

vcont = zeros(cont, dtype=int)
x = 0
for i in range(0, size(vet)):
	if vet[i] % 2 == 0:
		vcont[x] = i
		x = x + 1
		
print(cont)
print(vcont)

