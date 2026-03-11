d= input("Qual seu destino? ").lower()
i= float(input("Qual sua idade? "))

#preço das passagens
#Porto Velho
portovelho= 500.0
#Santarém
santarem= 370.0
#Belém
belem= 600.0
#Tefé
tefe= 360.0
#Tabatinga
tabatinga= 550.0

if((d != "porto velho") and (d != "santarem") and (d != "belem") and (d != "tefe") and (d != "tabatinga") and (i<0) and (i>150)):
	print("Entradas invalidas")
elif((i>0) and (i<=2)):
	print("Passagem: R$", portovelho * 0)
	print("Passagem: R$", santarem*0)
	print("Passagem: R$", belem*0)
	print("Passagem: R$", tefe*0)
	print("Passagem: R$", tabatinga*0)
elif((i>=3) and (i<=12)):
	print("Passagem: R$", portovelho/2)
	print("Passagem: R$", santarem/2)
	print("Passagem: R$", belem/2)
	print("Passagem: R$", tefe/2)
	print("Passagem: R$", tabatinga/2)
elif((i>=65) and(i<150)):
	print("Passagem: R$", portovelho*0.30)
	print("Passagem: R$", santarem*0.30)
	print("Passagem: R$", belem*0.30)
	print("Passagem: R$", tefe*0.30)
	print("Passagem: R$", tabatinga*0.30)












