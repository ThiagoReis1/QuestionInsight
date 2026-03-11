v = float(input("Informe o valor da velocidade:"))
t = float(input("Informe o valor do tempo:"))

if(v/t > 250):
	print("Hosgmed")
else:
	print("Entradas:", v/t, "km/h", "e", t, "h")
	print("Dados invalidos")