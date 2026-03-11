altura_cicero = 1.8
taxa_cicero = 0.01

altura = float(input("Altura do aluno: "))
taxa = float(input("taxa de crescimento do aluno: "))

anos = 0

while altura < altura_cicero:
	altura_cicero += taxa_cicero
	altura += taxa
	anos += 1

print(anos)