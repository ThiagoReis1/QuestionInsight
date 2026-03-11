altura_bia = 1.69
taxa_bia = 0.01

ano = 0

altura_aluno = float(input("digite a altura do aluno: "))
crescimento_aluno = float(input("digite a taxa de crescimento: "))

while altura_bia > altura_aluno:
	altura_bia = altura_bia + 0.01
	altura_aluno = altura_aluno + crescimento_aluno
	ano = ano + 1
print(ano)

	
