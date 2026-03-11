altura_cicero = 1.8
taxa_cicero = 0.01
altura_pessoa = float(input())
taxa_pessoa = float(input())
anos = 0
while altura_pessoa <= altura_cicero:
	altura_cicero += taxa_cicero
	altura_pessoa += taxa_pessoa
	anos += 1
print(anos)