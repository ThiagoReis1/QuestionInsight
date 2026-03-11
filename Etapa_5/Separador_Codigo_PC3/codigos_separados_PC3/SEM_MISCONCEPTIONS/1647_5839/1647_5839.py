from numpy import *

vetor = array(eval(input("Digite a frequencia: ")))
x = size(vetor)

aprovados = 0

for i in range(0,x):
	if (vetor[i] >= 70):
		aprovados = aprovados + 1

new = zeros(aprovados, dtype=int)
n = 0
	
for i in range(0,x):
	if (vetor[i] >= 70):
		new[n] = i
		n = n + 1

print(aprovados)
print(new)