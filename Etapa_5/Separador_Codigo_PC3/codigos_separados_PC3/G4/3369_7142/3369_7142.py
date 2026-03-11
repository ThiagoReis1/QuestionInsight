v = input("Informe a unidade em que a velocidade esta, M ou K: ")
vVelocidade = float(input("Informe o valor da velocidade: "))

uv = v.upper()

if(uv == "M"):
	vKm = 3.6*vVelocidade
	print(round(vKm, 2))
else:
	vMs = vVelocidade/3.6
	print(round(vMs, 2))
