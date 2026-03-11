from numpy import*
alunos = array(eval(input("frequencia: ")))
ac = 0
freq_nec = 70*0.1
reprovados = 0
j = 0

for i in range (size(alunos)):
	if alunos[i] * 0.1 < freq_nec:
		reprovados = reprovados + 1
	else:
		ac = ac + 1
print(ac)
aprovados = zeros(ac, dtype=int)
for i in range (size(alunos)):
	if alunos[i] * 0.1 < freq_nec:
		reprovados = reprovados + 1
	else:	
		aprovados[j] = i
		j = j + 1
print(aprovados)

		
	


