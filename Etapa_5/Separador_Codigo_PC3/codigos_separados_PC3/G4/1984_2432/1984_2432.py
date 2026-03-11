C = input("O resultado do time de futebol nessa competição: ")
P = input("Quantas vezes o time de futebol alcançou esse resultado: ")

if C == "CAMPEAO" and P == "11-VEZES":
	R= "REAL MADRID"
	print(R.upper())
elif C == "CAMPEAO" and P == "05-VEZES":
	R= "BARCELONA"
	print(R.upper())
elif C == "VICE-CAMPEAO" and P == "01-VEZ":
	R= "CHELSEA"
	print(R.upper())
elif C == "VICE-CAMPEAO" and P == "04-VEZES":
	R= "MILAN"
	print(R.upper())
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")