city=input("Cidade de destino: ")
idade=int(input("Digite a idade:"))
print("Entradas: " + city + " ,",idade)
	if (city=="Porto Velho") or (city=="Santarem") or (city=="Belem") or (city=="Tefe") or (city=="Tabatinga"):
	if  city=="Porto Velho":
		passagem=500.00
	if 0<=idade<=2:
		print("Passagem: R$",0)
	elif 3<=idade<=12:
		pas= passagem/2
		print("Passagem: R$",round(pas,2))
	elif 13<=idade<65:
		print("Passagem: R$",round(passagem,2))
	elif 65<=idade<=150:
		desc= passagem * 0.30
		pas1= passagem - desc
		print("Passagem: R$",round(pas1,2))
else:
	print("entradas invalidas")
elif  city=="Santarem":
passagem1=370.00
if 0<=idade<=2:
print("Passagem: R$",0)
elif 3<=idade<=12:
pas1= passagem1/2
print("Passagem: R$",round(pas1,2))
elif 13<=idade<65:
print("Passagem: R$",round(passagem1,2))
elif 65<=idade<=150:
desc1= passagem1 * 0.30
pas11= passagem1 - desc1
print("Passagem: R$",round(pas11,2))
else:
print("entradas invalidas")
elif  city=="Belem":
passagem2=600.00
if 0<=idade<=2:
print("Passagem: R$",0)
elif 3<=idade<=12:
pas2= passagem2/2
print("Passagem: R$",round(pas2,2))
elif 13<=idade<65:
print("Passagem: R$",round(passagem2,2))
elif 65<=idade<=150:
desc2= passagem2 * 0.30
pas12= passagem2 - desc2
print("Passagem: R$",round(pas12,2))
else:
print("entradas invalidas")
elif  city=="Tefe":
passagem3=360.00
if 0<=idade<=2:
print("Passagem: R$",0)
elif 3<=idade<=12:
pas3= passagem3/2
print("Passagem: R$",round(pas3,2))
elif 13<=idade<65:
print("Passagem: R$",round(passagem3,2))
elif 65<=idade<=150:
desc3= passagem3 * 0.30
pas13= passagem3 - desc3
print("Passagem: R$",round(pas13,2))
else:
print("entradas invalidas")
elif  city=="Tabatinga":
passagem4=550.00
if 0<=idade<=2:
print("Passagem: R$",0)
elif 3<=idade<=12:
pas4= passagem4/2
print("Passagem: R$",round(pas4,2))
elif 13<=idade<65:
print("Passagem: R$",round(passagem4,2))
elif 65<=idade<=150:
desc4= passagem4 * 0.30
pas14= passagem4 - desc4
print("Passagem: R$",round(pas14,2))
else:
print("entradas invalidas")
else:
print("entradas invalidas")