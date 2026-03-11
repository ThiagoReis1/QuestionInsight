velocidade=float(input("velocidade"))

minutos=0

while (velocidade>= 50):
	print(round(velocidade,2))
	velocidade=velocidade-velocidade*0.25
	minutos=minutos+1
	
	