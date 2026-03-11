from numpy import*

vetor = array(eval(input("NOta dos alunos: ")))

r = 0

for i in range(size(vetor)):
	if(vetor[i]<5.0):
		r = r + 1
		
print(r)

cont = zeros(r, dtype=int)
rp = 0

for m in range(size(vetor)):
	if(vetor[m]<5.0):
		cont[rp] = m
		rp = rp + 1

print(cont)

		

		



