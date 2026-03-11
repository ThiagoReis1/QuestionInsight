altura=float(input("Digite:"))
sexo=input().upper()
if (altura<1.0) or (altura>2.5):
	print("altura invalida")
elif (sexo!="M") and (sexo!="F"):
	print("codigo invalido de sexo")
elif:(sexo=="M"):
	Homem=(72.7*altura)-58
	print(round(homem,2))
elif:(sexo=="F"):
	Mulher=(62.1*altura)-44.7
	print(round(mulher,2))