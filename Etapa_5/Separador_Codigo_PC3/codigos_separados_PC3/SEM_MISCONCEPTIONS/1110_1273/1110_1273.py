prato = int(input("Entre com o  prato: "))

sobremesa = int(input ("Entre com a sobremesa: "))

bebida = int(input("Entre com a bebida: "))

cal_vegetariano = 180

cal_peixe = 230

cal_frango = 250

cal_carne = 350

cal_abacaxi = 75

cal_sorvete = 110

cal_mouse = 170

cal_mouse_c = 200

cal_cha = 20

suco_de_laranja = 70

suco_de_melao = 100

refrigerante = 65

if (prato == 1 ):
	if (sobremesa == 1 ):
		if ( bebida == 1):
			calorias = cal_vegetariano + cal_abacaxi + cal_cha
		elif (bebida == 2):
			calorias = cal_vegetariano + cal_abacaxi + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_vegetariano + cal_abacaxi + suco_de_melao
		else:
			calorias = cal_vegetariano + cal_abacaxi + refrigerante
	elif (sobremesa == 2 ):
		if ( bebida == 1):
			calorias = cal_vegetariano + cal_sorvete + cal_cha
		elif (bebida == 2):
			calorias = cal_vegetariano + cal_sorvete + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_vegetariano + cal_sorvete + suco_de_melao
		else:
			calorias = cal_vegetariano + cal_sorvete + refrigerante
	elif (sobremesa == 3 ):
		if ( bebida == 1):
			calorias = cal_vegetariano + cal_mouse + cal_cha
		elif (bebida == 2):
			calorias = cal_vegetariano + cal_mouse + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_vegetariano + cal_mouse + suco_de_melao
		else:
			calorias = cal_vegetariano + cal_mouse + refrigerante
	else:
		if ( bebida == 1):
			calorias = cal_vegetariano + cal_mouse_c + cal_cha
		elif (bebida == 2):
			calorias = cal_vegetariano + cal_mouse_c + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_vegetariano + cal_mouse_c + suco_de_melao
		else:
			calorias = cal_vegetariano + cal_mouse_c + refrigerante
elif (prato == 2 ):
	if (sobremesa == 1 ):
		if ( bebida == 1):
			calorias = cal_peixe + cal_abacaxi + cal_cha
		elif (bebida == 2):
			calorias = cal_peixe + cal_abacaxi + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_peixe + cal_abacaxi + suco_de_melao
		else:
			calorias = cal_peixe + cal_abacaxi + refrigerante
	elif (sobremesa == 2 ):
		if ( bebida == 1):
			calorias = cal_peixe + cal_sorvete + cal_cha
		elif (bebida == 2):
			calorias = cal_peixe + cal_sorvete + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_peixe + cal_sorvete + suco_de_melao
		else:
			calorias = cal_peixe + cal_sorvete + refrigerante
	elif (sobremesa == 3 ):
		if ( bebida == 1):
			calorias = cal_peixe + cal_mouse + cal_cha
		elif (bebida == 2):
			calorias = cal_peixe + cal_mouse + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_peixe + cal_mouse + suco_de_melao
		else:
			calorias = cal_peixe + cal_mouse + refrigerante
	else:
		if ( bebida == 1):
			calorias = cal_peixe + cal_mouse_c + cal_cha
		elif (bebida == 2):
			calorias = cal_peixe + cal_mouse_c + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_peixe + cal_mouse_c + suco_de_melao
		else:
			calorias = cal_peixe + cal_mouse_c + refrigerante
elif (prato == 3 ):
	if (sobremesa == 1 ):
		if ( bebida == 1):
			calorias = cal_frango + cal_abacaxi + cal_cha
		elif (bebida == 2):
			calorias = cal_frango + cal_abacaxi + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_frango + cal_abacaxi + suco_de_melao
		else:
			calorias = cal_frango + cal_abacaxi + refrigerante
	elif (sobremesa == 2 ):
		if ( bebida == 1):
			calorias = cal_frango + cal_sorvete + cal_cha
		elif (bebida == 2):
			calorias = cal_frango + cal_sorvete + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_frango + cal_sorvete + suco_de_melao
		else:
			calorias = cal_frango + cal_sorvete + refrigerante
	elif (sobremesa == 3 ):
		if ( bebida == 1):
			calorias = cal_frango + cal_mouse + cal_cha
		elif (bebida == 2):
			calorias = cal_frango + cal_mouse + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_frango + cal_mouse + suco_de_melao
		else:
			calorias = cal_frango + cal_mouse + refrigerante
	else:
		if ( bebida == 1):
			calorias = cal_frango + cal_mouse_c + cal_cha
		elif (bebida == 2):
			calorias = cal_frango + cal_mouse_c + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_frango + cal_mouse_c + suco_de_melao
		else:
			calorias = cal_frango + cal_mouse_c + refrigerante
elif (prato == 4 ):
	if (sobremesa == 1 ):
		if ( bebida == 1):
			calorias = cal_carne + cal_abacaxi + cal_cha
		elif (bebida == 2):
			calorias = cal_carne + cal_abacaxi + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_carne + cal_abacaxi + suco_de_melao
		else:
			calorias = cal_carne + cal_abacaxi + refrigerante
	elif (sobremesa == 2 ):
		if ( bebida == 1):
			calorias = cal_carne + cal_sorvete + cal_cha
		elif (bebida == 2):
			calorias = cal_carne + cal_sorvete + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_carne + cal_sorvete + suco_de_melao
		else:
			calorias = cal_carne + cal_sorvete + refrigerante
	elif (sobremesa == 3 ):
		if ( bebida == 1):
			calorias = cal_carne + cal_mouse + cal_cha
		elif (bebida == 2):
			calorias = cal_carne + cal_mouse + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_carne + cal_mouse + suco_de_melao
		else:
			calorias = cal_carne + cal_mouse + refrigerante
	else:
		if ( bebida == 1):
			calorias = cal_carne + cal_mouse_c + cal_cha
		elif (bebida == 2):
			calorias = cal_carne + cal_mouse_c + suco_de_laranja
		elif (bebida == 3):
			calorias = cal_carne + cal_mouse_c + suco_de_melao
		else:
			calorias = cal_carne + cal_mouse_c + refrigerante
else:
	calorias = -1

print("Entradas: ", prato, ",", sobremesa, ",", bebida)
if (calorias != -1):
	print("Calorias: ", calorias, "cal")
else:
	print("Dados invalidos")