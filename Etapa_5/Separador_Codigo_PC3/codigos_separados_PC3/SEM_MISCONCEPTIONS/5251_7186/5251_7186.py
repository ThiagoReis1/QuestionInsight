from math import*
D= input("Cidade de destino: ")
I= int(input("Idade do passageiro: "))

print("Entradas:", D, ",", I)

if(3 >= I <= 12 and D=="porto velho"):
	V= 500 - 500*(50/100)
	print(round(("Passagem: R$", V), 2))
elif(I >= 65 and D == "porto velho"):
	V= 500 - 500*(30/100)
	print(round(("Passagem: R$", V), 2))
elif(3 >=I<=12 and D=="santarem"):
	V= 370 - 370*(50/100)
	print(round(("Passagem: R$", V), 2))
elif(I>=65 and D=="santarem"):
	V= 370 -370*(30/100)
	print(round(("Passagem: R$", V), 2))
elif(3>=I<=12 and D=="belem"):
	V=600 - 600*(50/100)
	print(round(("Passagem: R$", V), 2))
elif(I>=65 and D=="belem"):
	V= 600 - 600*(50/100)
	print(round(("Passagem: R$", V), 2))
elif(3>=I<=12 and D=="tefe"):
	V= 360- 360*(50/100)
	print(round(("Passagem: R$", V), 2))
elif(I>=65 and D=="tefe"):
	V= 360 - 360*(30/100)
	print(round(("Passagem: R$", V), 2))
elif(3>=I<=12 and D=="tabatinga"):
	V= 550-550*(50/100)
	print(round(("Passagem: R$", V), 2))
elif(I>=65 and D=="tabatinga"):
	V= 550-550*(30/100)
	print(round(("Passagem: R$", V), 2))
elif(D!="porto velho" or D!="santarem" or D!="belem" or D!="tefe" or D!="tabatinga")
	print("entradas invalidas")
elif(0>=I>=150):
	print("invalidas")

		

	