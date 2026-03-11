ent = float(input("preço normal da entrada:"))
dds = int(input("dia da semana:"))
mav = input("Eh dia de música ao vivo? (S/N):")
print("Entradas:", round(ent,2),",",dds,",",mav)
ent_desc =(ent*0.25)
if (dds>=1) and (dds<=7):
	if(mav == "S"):
		if (dds ==1):
			precoent = ent
		elif (dds ==2):
			precoent = ent - ent_desc
		elif (dds ==3):
			precoent = ent - ent_desc
		elif (dds ==4):
			precoent = ent
		elif (dds ==5):
			precoent = ent - ent_desc
		elif (dds ==6):
			precoent = ent
		elif (dds ==7):
			precoent = ent
		print("Valor a pagar: R$",round(ent_desc,2)+20)
	else:
		print("Valor a pagar: R$",round(ent_desc,2))
else:
	print("Dados invalidos")

	
