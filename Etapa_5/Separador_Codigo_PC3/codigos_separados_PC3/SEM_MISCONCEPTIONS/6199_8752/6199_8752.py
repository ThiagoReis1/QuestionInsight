altura_cicero = 1.8
taxa_cicero = 0.01

altura_pessoa = float(input("altura do mano: "))
taxa_de_crescimento = float(input("taxa de crescimento: "))

anos = 0

while altura_cicero > altura_pessoa:
	altura_cicero = altura_cicero + taxa_cicero
	altura_pessoa = altura_pessoa + taxa_de_crescimento
	anos += 1

print(anos)	
	