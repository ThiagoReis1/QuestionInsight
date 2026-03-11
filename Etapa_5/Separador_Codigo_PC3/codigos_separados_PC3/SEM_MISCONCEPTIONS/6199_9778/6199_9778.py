altura_cicero = 1.8
taxa_cicero = 0.01

altura_alunox = float(input())
taxa_alunox = float(input())

ano = 0

while(altura_alunox<=altura_cicero):
	altura_cicero = altura_cicero + taxa_cicero
	altura_alunox = altura_alunox + taxa_alunox
	
	ano += 1
print(ano)