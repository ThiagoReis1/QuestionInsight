from numpy import*

freq = array(eval(input("Frequencia do aluno: ")))
porct = 70
a = 0

for i in range(size(freq)):
	if freq[i] >= porct: 
		a += 1
print(a)

grupoa = zeros(a, dtype=int)

cont = 0

for i in range(size(freq)):
	#grupoa[cont] = freq[i]
	#cont += 1
	if freq[i] >= porct:
		grupoa[cont] = i
		cont += 1
print(grupoa)