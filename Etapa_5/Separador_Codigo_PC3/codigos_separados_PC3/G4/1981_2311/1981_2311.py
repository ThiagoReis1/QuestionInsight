A = input("O resultado do time de futebol nessa competição: ")
B = input("Quantas vezes o time de futebol alcançou esse resultado: ")

if A == "Campeao" and B == "06-vezes":
	R= "CORINTHIANS"
	print(R.upper())
elif A == "Campeao" and B == "03-vezes":
	R= "SANTOS"
	print(R.upper())
elif A == "Vice-Campeao" and B == "01-vez":
	R= "FLAMENGO"
	print(R.upper())
elif A == "Vice-Campeao" and B == "06-vezes":
	R= "INTERNACIONAL"
	print(R.upper())
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")