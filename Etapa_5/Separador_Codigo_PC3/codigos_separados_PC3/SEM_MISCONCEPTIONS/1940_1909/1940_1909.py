#inicio program
nome_mol = input("digite o nome da molecula:")
#valores dos dados das moleculas 
oxi = 15.9994
carb = 12.011
nitrg = 14.0067
hidrg = 1.00794
#calculo do peso molecular 
PeM_glu = (5 * carb) + (8 * hidrg) + (1 * nitrg) + (4 * oxi)
PeM_treo = (4 * carb) + (9 * hidrg) + (1 * nitrg) + (3 * oxi)
#condicao 
if(nome_mol.upper() == "GLUTAMINA"):
	print(round(PeM_glu,2))
else:
	print(round(PeM_treo,2))