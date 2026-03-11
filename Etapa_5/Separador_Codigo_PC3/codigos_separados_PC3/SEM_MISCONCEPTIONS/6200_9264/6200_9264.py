altura_max = 1.75
taxa_max = 0.01
anos = 0 

altura_aluno = float(input("Digite a altura do outro aluno: "))
taxa_aluno = float(input("Digite a taxa de crescimento do outro aluno: "))

while altura_aluno < altura_max:
	altura_max = altura_max + taxa_max
	altura_aluno = altura_aluno + taxa_aluno
	anos = anos+1
print(anos)
	