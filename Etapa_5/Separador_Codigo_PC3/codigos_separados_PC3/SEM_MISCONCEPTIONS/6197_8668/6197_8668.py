altura_alice = 1.6
taxa_alice = 0.02

altura_aluno = float(input())
taxa_aluno = float(input())
anos = 0 

while (altura_aluno < altura_alice):
	altura_alice += taxa_alice
	altura_aluno += taxa_aluno
	anos += 1
print(anos)
	