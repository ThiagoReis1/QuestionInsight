altura_cicero = 1.8
taxa_cicero = 0.01

alt_pessoa = float(input("Altura: "))
taxa_pessoa = float(input("taxa: "))

ano = 0

while alt_pessoa < altura_cicero:
	altura_cicero = altura_cicero + taxa_cicero
	alt_pessoa = alt_pessoa + taxa_pessoa
	
	ano += 1

print(ano)
