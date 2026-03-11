lanc = input("resultado do lancamento: ").upper()
tlanc = 0
while lanc != "S":
	if lanc == "CARA":
		tlanc = tlanc + 1
	lanc = input("resultado do lancamento: ").upper()

print(tlanc)

	