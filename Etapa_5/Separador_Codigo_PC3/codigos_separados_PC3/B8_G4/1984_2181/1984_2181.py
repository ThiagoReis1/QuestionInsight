c1 = input("Digite a primeira caracteristica: ")
c2 = input("Digite a segunda caracteristica: ")

if(c1.upper() != 'CAMPEAO' and c1.upper() != 'VICE-CAMPEAO' or c2.upper() != '11-VEZES' and c2.upper() != '05-VEZES' and c2.upper() != '01-VEZ' and c2.upper() != '04-VEZES' ):
	print("TIME DE FUTEBOL NAO IDENTIFICADO")
else:
	if(c1.upper() == 'CAMPEAO' and c2.upper() == '11-VEZES'):
		print("REAL MADRID")
	elif(c1.upper() == 'CAMPEAO' and c2.upper() == '05-VEZES'):
		print("BARCELONA")
	elif(c1.upper() == 'VICE-CAMPEAO' and c2.upper() == '01-VEZ'):
		print("CHELSEA")
	elif(c1.upper() == 'VICE-CAMPEAO' and c2.upper() == '04-VEZES'):
		print("MILAN")
