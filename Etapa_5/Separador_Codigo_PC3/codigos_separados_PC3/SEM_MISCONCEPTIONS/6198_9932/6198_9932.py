altura_luna = 1.65
taxa_luna = 0.02
altura_aluno = float(input())
taxa_aluno = float(input())
anos = 0
while altura_luna >= altura_aluno:
	altura_luna = altura_luna + taxa_luna
	altura_aluno = altura_aluno + taxa_aluno
	anos+= 1
print(anos)