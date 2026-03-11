r = input("digite o resultado do time de futebol")
v = input("digite quantas vezes o time de futebol alcançou esse resultado")

if(r != "Campeao" and r != "Vice-campeao") or (v != "06-vezes" and v != "03-vezes" and v != "01-vezes"):
	print("TIME DE FUTEBOL NAO IDENTIFICADO")
else:
	if r == "Campeao" and v == "06-vezes":
		X = "Corinthians"
		print(X.upper())
	elif r == "Campeao" and v == "03-vezes":
		X = "Santos"
		print(X.upper())
	elif r == "Vice-campeao" and v == "01-vezes":
		X = "Flamengo"
		print(X.upper())
	elif r == "Vice-campeao" and v == "06-vezes":
		X = "Internacional"
		print(X.upper())
