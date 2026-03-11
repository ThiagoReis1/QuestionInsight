unidade=input("Digite M ou K:")
velocidade=float(input("Digite a velocidade:"))

if (unidade == "M"):
	print(round(velocidade*3.6 ,2) )
if (unidade == "K"):
	print(round(velocidade/3.6 ,2) )