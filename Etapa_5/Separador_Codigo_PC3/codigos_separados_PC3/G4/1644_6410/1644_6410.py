from numpy import *

vet = array(eval(input("notas: ")))
s = 0

for i in vet:
	if i < 5:
		s = s + 1
vet_final = zeros(s,dtype=int)
j = 0
k = 0

for i in vet :
	if i < 5:
		vet_final[k] = j
		k = k + 1
	j = j + 1
print(s)
print(vet_final)