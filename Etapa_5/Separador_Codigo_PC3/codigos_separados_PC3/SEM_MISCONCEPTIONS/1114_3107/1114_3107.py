velocidade = float(input())
tempo = float(input())

print("Entradas:", velocidade,"km/h e", tempo,"h")

tempo = velocidade * tempo;
if velocidade <= 0 or tempo < 0:
	print("Dados invalidos")
elif tempo < 100:
	print("Proxima parada: Bravos")
elif tempo < 200 :
	print("Proxima parada: Castamere")
elif tempo < 400:
	print("Proxima parada: Doriath")
elif tempo < 600:
	print("Proxima parada: Edoras")
elif tempo < 750:
	print("Proxima parada: Fangorn")
elif tempo < 1150:
	print("Proxima parada: Gondor")
else:
	print("Proxima parada: Hogsmead")
