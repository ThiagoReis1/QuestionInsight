chico = 1.5
taxa_chico = 0.02

altura = float(input("altura do aluno: "))
taxa = float(input("taxa de crescimento: "))

temp = 0

while altura < chico:
	chico = chico + 0.02
	altura = altura + taxa
	temp = temp + 1
print(temp)
	