vt = float(input("Qual a velocidade do trem: "))
tempo = float(input("Qual o tempo de viagem: "))
distancia_total = 1400
tempo_total = distancia_total / vt
distancia = vt * tempo
print("Entradas:", vt,"km/h e", tempo, "h")
if(vt <= 0 or tempo <= 0):
	x = "invalido"
elif(distancia < 100 and distancia >= 0):
	x = "Bravos"
elif(distancia < 200 and distancia >= 100):
	x = "Castamare"
elif(distancia < 400 and distancia >= 200):
	x = "Doriath"
elif(distancia < 500 and distancia >= 200):
	x= "Edoras"
elif(distancia < 750 and distancia >= 600):
	x = "Fangorn"
elif(distancia < 1150 and distancia >= 750):
   x = "Gondor"
else:
	x= "Hogsmead"

if( x == "invalido" ):
	print("Dados invalidos")
else:
	print("Proxima parada:", x)