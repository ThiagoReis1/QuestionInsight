altura_alice = 1.6
taxa_alice = 0.02

altura_aluno=float(input("altura do aluno "))
taxa=float(input("tx"))

contador=0

while(altura_alice > altura_aluno):
	altura_alice = altura_alice + taxa_alice
	altura_aluno = altura_aluno + taxa
	contador = contador + 1
	
print(contador)
	
	
	
