altura_chico = 1.5
taxa_chico = 0.02
altura_aluno = float(input("altura do aluno: "))
taxa_aluno = float(input("taxa de crescimento do aluno: "))

anos = 0

while altura_aluno < altura_chico:
	altura_chico += taxa_chico
	altura_aluno += taxa_aluno
	anos = anos + 1
	
print(anos)