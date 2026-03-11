vara = input("S ou T: ")
varb = int(input("Quantidade: "))
varc = int(input("Quantidade: "))


vartap = (5.50*varb)
varsal = (4.00*varb)
varaca = (10.00*varc)
if vara == "S":
	valortot = varsal+varaca
	print(round(valortot,2))
else:
	valortot = vartap+varaca
	print(round(valortot,2))

