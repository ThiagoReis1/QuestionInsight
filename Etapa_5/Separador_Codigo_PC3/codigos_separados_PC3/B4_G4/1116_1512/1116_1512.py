#Universidade Federal do Amazonas
#Marcos Stephano Maia de Lima - 21602344
#21 / 07 / 2016
x = input("coordenada x:")
y = input("coordenada y:")

if((x == 1.0) and (y == 2.5)):
	print("quandrante 1")
elif((x == -1.0) and (y == -2.5)):
	print("quandrante 3")
elif((x == 0.0) and (y == -2.5)):
	print("estah situado sobre um dos eixos")
elif((x == 0.0) and (y == 0.0)):
	print("estah situado sobre um dos eixos")
else:
	print