from numpy import *

notas = array(eval(input("Notas dos estudantes: ")))
cont = 0

for i in notas:
	if (i >= 5):
		cont = cont + 1
print(cont)

vet = zeros(size(cont), dtype=int)
for i in notas:
	if (i >= 5):
		vet[] =[i]
print(vet)