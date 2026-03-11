des= input()
ida= int(input())
print("Entradas: " + des + " ,",ida)
if (des=="Porto Velho") or (des=="Santarem") or (des=="Belem") or (des=="Tefe") or (des=="Tabatinga"):
	if  des=="Porto Velho":
		passagem=500.00
		if 0<=ida<=2:
			print("Passagem: R$",0)
		elif 3<=ida<=12:
			pas= passagem/2
			print("Passagem: R$",round(pas,2))
		elif 13<=ida<65:
			print("Passagem: R$",round(passagem,2))
		elif 65<=ida<=150:
			desc= passagem * 0.30
			pas1= passagem - desc
			print("Passagem: R$",round(pas1,2))
		else:
			print("entradas invalidas")
	elif  des=="Santarem":
			passagem1=370.00
			if 0<=ida<=2:
				print("Passagem: R$",0)
			elif 3<=ida<=12:
				pas1= passagem1/2
				print("Passagem: R$",round(pas1,2))
			elif 13<=ida<65:
				print("Passagem: R$",round(passagem1,2))
			elif 65<=ida<=150:
				desc1= passagem1 * 0.30
				pas11= passagem1 - desc1
				print("Passagem: R$",round(pas11,2))
			else:
				print("entradas invalidas")
	elif  des=="Belem":
			passagem2=600.00
			if 0<=ida<=2:
				print("Passagem: R$",0)
			elif 3<=ida<=12:
				pas2= passagem2/2
				print("Passagem: R$",round(pas2,2))
			elif 13<=ida<65:
				print("Passagem: R$",round(passagem2,2))
			elif 65<=ida<=150:
				desc2= passagem2 * 0.30
				pas12= passagem2 - desc2
				print("Passagem: R$",round(pas12,2))
			else:
				print("entradas invalidas")
	elif  des=="Tefe":
			passagem3=360.00
			if 0<=ida<=2:
				print("Passagem: R$",0)
			elif 3<=ida<=12:
				pas3= passagem3/2
				print("Passagem: R$",round(pas3,2))
			elif 13<=ida<65:
				print("Passagem: R$",round(passagem3,2))
			elif 65<=ida<=150:
				desc3= passagem3 * 0.30
				pas13= passagem3 - desc3
				print("Passagem: R$",round(pas13,2))
			else:
				print("entradas invalidas")
	elif  des=="Tabatinga":
			passagem4=550.00
			if 0<=ida<=2:
				print("Passagem: R$",0)
			elif 3<=ida<=12:
				pas4= passagem4/2
				print("Passagem: R$",round(pas4,2))
			elif 13<=ida<65:
				print("Passagem: R$",round(passagem4,2))
			elif 65<=ida<=150:
				desc4= passagem4 * 0.30
				pas14= passagem4 - desc4
				print("Passagem: R$",round(pas14,2))
			else:
				print("entradas invalidas")
else:
	print("entradas invalidas")