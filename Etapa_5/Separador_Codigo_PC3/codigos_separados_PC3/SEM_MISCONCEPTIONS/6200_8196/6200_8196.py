altura_cicero = 1.75
taxa_cicero = 0.01

altm = float(input("digite a altura de max: "))
taxm = float(input("digite a taxa de max: "))
ano = 0

while (altura_cicero > altm):
	ano = ano + 1
	altura_cicero = altura_cicero + taxa_cicero
	altm = altm + taxm
	

print(ano)

	 