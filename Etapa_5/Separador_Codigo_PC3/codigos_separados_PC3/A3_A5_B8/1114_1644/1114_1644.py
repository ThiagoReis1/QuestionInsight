from math import sqrt
velocidade=float(input("digite o valor da velocidade:"))
hora=float(input("digite a quantidade de hora:"))
distancia= velocidade*hora
parada= "Avalon"
if(velocidade > 0 and hora > 0):
		if(distancia < 100):
			parada= "Bravos"
		elif(distancia < 200):
			parada= "Castamere"
		elif(distancia < 400):
			parada= "Doriath"
		elif(distancia < 600):
			parada= "Edoras"
		elif(distancia < 750):
			parada= "Fangorn"
		elif(distancia < 1150):
			parada= "Gondor"
		elif(distancia < 1400):
			parada= "Hogsmead"
		print("Entradas:",velocidade, "km/h e ",hora, "h")
		print("Proxima parada:", parada)
else:
		print("Entradas:",velocidade, "km/h e ",hora, "h")
		print("Dados invalidos")
	
			
			
			
			
			
			











