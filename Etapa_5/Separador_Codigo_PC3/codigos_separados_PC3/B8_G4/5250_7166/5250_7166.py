v = float(input("Digite velocidade em km/h: "))
t = float()
(input("Digite tempo em horas: "))

print("Entradas: ", vel, "km/h", temp, "h")

sp = v*t

if(v<= 0 or t< 0):
	print("dados invalidos")
elif( sp >= 0 and sp< 100):
	print("Proxima parada: Bravos")
elif(100 <= sp and sp <200):
	print("Proxima parada: Castamere")
elif(200 <= sp and sp<400):
	print("Proxima parada: Doriath")
elif( 400 <= sp and sp <600):
	print("Proxima parada: Edoras")
elif( 600<= sp and sp < 750):
	print("proxima parada: Fangorn")
elif(750 <= sp and sp <  1150):
	print("proxima parada: Gondor")
elif(1150 <= sp):
	print("proxima parada: Hogsmead")
