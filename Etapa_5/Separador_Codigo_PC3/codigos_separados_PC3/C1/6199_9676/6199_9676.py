altura_cicero = 1.8
taxa_cicero = 0.01

altura_aluno = float(input())
taxa_aluno = float(input())

cont = 0

while altura_aluno <= altura_cicero:
	altura_cicero = altura_cicero + taxa_cicero
	altura_aluno = altura_aluno + taxa_aluno
	cont += 1
	
	if altura_aluno > altura_cicero:
		print(cont)