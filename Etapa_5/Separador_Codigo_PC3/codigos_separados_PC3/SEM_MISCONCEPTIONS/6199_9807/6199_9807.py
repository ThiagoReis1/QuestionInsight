altura_cicero = 1.8
taxa_cicero = 0.01
cont = 0
altura = float(input("digite sua altura: "))
crescimento = float(input("figite sua atxa de crescimentpo: "))

while altura < altura_cicero:
	altura_cicero += taxa_cicero
	altura += crescimento
	cont += 1 
print(cont)
	
