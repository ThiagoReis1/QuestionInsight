altura_cicero = 1.8
taxa_cicero = 0.01

altura_pessoa = float(input('altura da pessoa '))
taxa_pessoa = float(input('taxa da pessoa'))
ano= 0

while altura_cicero >= altura_pessoa:
	altura_cicero = altura_cicero + taxa_cicero
	altura_pessoa = altura_pessoa + taxa_pessoa
	ano += 1
	
print(ano)