###################################
#
# Paulo Sergio da Silva Freitas
#
# Determinar o proximo destinop do trem
#
###################################

import math
velocidade = float(input("Qual a velocidade do trem km/h : "))
tempo = float(input("Qual o tempo de viagem : "))

if(velocidade <= 0.0 or tempo <= 0.0):
	print("Entradas:",velocidade,"km/h e",tempo," h")
	print("Dados invalidos")
else:
	distancia = velocidade*tempo
	if(0 < distancia < 100 ):
		proxima = "Bravos"
	elif (100 <= distancia < 200):
			proxima = "Castamere"
	elif (200 <= distancia < 400):
			proxima = "Doriath"
	elif (400 < distancia < 600):
			proxima = "Edoras"
	elif (600 < distancia < 750):
			proxima = "Fangorn"
	elif (750 < distancia < 1150):
			proxima = "Gondor"
	elif (1150 < distancia < 1400):
			proxima = "hogsmead"		

print("Entradas:",velocidade,"km/h e",tempo," h")
print("Proxima parada:",proxima)
print("distancia",distancia)
			
		





