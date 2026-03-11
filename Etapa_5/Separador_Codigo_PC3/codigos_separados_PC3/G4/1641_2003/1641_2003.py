from numpy import*

turmas = array(eval(input("Insira o número de alunos de cada turma: ")))
n = 0 #variável acumuladora de trios
 
for x in turmas:
	if x % 3 == 0:
		n = n + 1


new = zeros(n, dtype=int)
i = 0
k = 0
for x in turmas:
	if x % 3 == 0:
		new[i] = k
		i = i + 1
	k = k + 1

print(n)	
print(new)
		