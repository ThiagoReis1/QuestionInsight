valor_comp = float(input("valor da compra: "))

pagam = input("D para dinheiro, P para pix e C para cartao: ").upper()

if pagam == "D" or pagam == "P":
	desc= valor_comp * (13/100)
	valor_tot= valor_comp - desc
	print(round(valor_tot, 2))
	
elif pagam == "C":
	vezezz= int(input("quantas vezes? "))
	if vezezz == 1:
		valor_tot = valor_comp
		print(round(valor_tot, 2))
		
	else:
		jur= valor_comp * (8/100)
		valor_tot = valor_comp + jur
		print(round(valor_tot,2))