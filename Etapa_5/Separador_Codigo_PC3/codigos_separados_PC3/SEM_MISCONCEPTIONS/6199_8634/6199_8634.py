altura_cicero = 1.8
taxa_cicero = 0.01
altura_pessoa = float(input("Altura da pessoa: "))
taxa_pessoa = float(input("Taxa de crescimento da pessoa: "))
ano = 0

while altura_cicero > altura_pessoa:
	
	altura_pessoa += (taxa_pessoa)
	altura_cicero += (taxa_cicero)
	
	ano += 1
	
print(ano)