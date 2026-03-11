valor = float(input("valor da mensalidade: "))
c = int(input("numero de criancas: "))

if c == 1:
	taxa = (valor - valor*(10/100))*c
	print(round(taxa, 2))
if c == 2:
	taxa = ( valor - valor *(30/100))*c
	print(round(taxa, 2))
if c >= 3:
	taxa = (valor - valor*(40/100))*c
	print(round(taxa, 2))
	