altura_max = 1.75
taxa_max = 0.01

altura_aluno = float(input())
taxa_aluno = float(input())

c = 0

while (altura_aluno < altura_max):
	altura_aluno = altura_aluno+ taxa_aluno
	altura_max = altura_max +0.01
	
	c = c + 1

print(c)