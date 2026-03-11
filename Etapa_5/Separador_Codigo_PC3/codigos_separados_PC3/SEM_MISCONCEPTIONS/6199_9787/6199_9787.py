altura_cicero = 1.8
taxa_cicero = 0.01

altura_pc = float(input(""))
taxa_pc = float(input(""))

ano = 0

while (altura_cicero > altura_pc):
	altura_cicero = altura_cicero + taxa_cicero
	altura_pc = altura_pc + taxa_pc
	ano += 1


print(ano)
	
