alta = 1.6
taxaa = 0.02
cont = 0

alt = float(input("Digite a altura:"))
taxa = float(input("Digite a taxa:"))

while alta > alt:
	alt = alt + taxa
	cont = cont + 1
	alta = alta + taxaa
	if alta <= alt:
		print(cont)
