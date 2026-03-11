altura_luna = 1.65
taxa_luna = 0.02
aluno = 1.42
taxa_aluno = 0.06
soma = 0

float(input("altura: "))
float(input("taxa de crescimento: "))

while (aluno > altura_luna):
	altura_luna = altura_luna + taxa_luna 
	aluno = aluno + taxa_aluno
	soma = soma + 6
print(soma)

	
