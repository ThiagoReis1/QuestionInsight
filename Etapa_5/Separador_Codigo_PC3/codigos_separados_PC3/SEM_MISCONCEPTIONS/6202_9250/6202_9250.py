altura_bia = 1.69
taxa_bia = 0.01

altura_aluno = float(input())
taxa_aluno = float(input())

ano = 0

while altura_aluno <= altura_bia:
	altura_aluno = altura_aluno + taxa_aluno
	altura_bia += taxa_bia
	ano = ano + 1
	
print(ano)