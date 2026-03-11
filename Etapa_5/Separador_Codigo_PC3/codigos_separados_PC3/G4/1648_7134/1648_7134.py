from numpy import *
alu = array(eval(input("alunos: ")))
rep = 0
j = zeros(size(alu), dtype=int)

for i in range(size(alu)):
	if alu[i] < 70:
		rep = rep + 1
		j[i] = i
		
print(rep)

apro = zeros(rep, dtype=int)
a = 0

for i in range(size(alu)):
	if alu[i] < 70:
		apro[a] = i
		a = a + 1

print(apro)