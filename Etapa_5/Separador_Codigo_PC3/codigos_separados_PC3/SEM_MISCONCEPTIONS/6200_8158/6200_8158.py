altura_aluno = float(input("Digite a altura do aluno: "))
taxa_aluno = float(input("Digite a taxa do aluno: "))

altura_max = 1.75
taxa_max = 0.01
tempo = 0


while altura_aluno < altura_max:
	altura_aluno = altura_aluno + (taxa_aluno)
	tempo = tempo + 1
	altura_max = altura_max + taxa_max
	
print(tempo)



	
		
		

