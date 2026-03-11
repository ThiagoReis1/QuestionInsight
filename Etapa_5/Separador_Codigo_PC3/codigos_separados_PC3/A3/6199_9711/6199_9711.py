altura_cicero = 1.8
taxa_cicero = 0.01
taxa_crescimento_cicero = 0.01

altura = float(input())
taxa_pessoa = float(input())

anos = 0
while altura <= altura_cicero:
	altura_cicero += taxa_cicero
	altura += taxa_pessoa
	anos += 1 
print(anos)