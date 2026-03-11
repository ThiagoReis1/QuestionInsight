altura = float(input())
taxa = float(input())
cont = 0

altura_cicero = 1.75
taxa_cicero = 0.01
while (altura < altura_cicero):
	altura = altura + taxa
	altura_cicero = altura_cicero + taxa_cicero
	cont =cont + 1
print(cont)


