altura_joe = 1.77
taxa_joe = 0.02
altura_aluno = float(input(""))
taxa_aluno = float(input(""))
anos = 0
while(altura_aluno < altura_joe):
	altura_joe=altura_joe+taxa_joe
	altura_aluno=altura_aluno+taxa_aluno
	anos+=1
print(anos)