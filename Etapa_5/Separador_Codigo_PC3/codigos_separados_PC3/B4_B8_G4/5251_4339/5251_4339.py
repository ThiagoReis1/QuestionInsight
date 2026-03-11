c= input("cidade de destino:")
i= int(input("idade:"))

print("Entradas:",c,",",i)

if(c == "Porto Velho") or (c == "Santarem") or (c == "Belem") or (c == "Tefe") or (c == "Tabatinga") and (i > 0) and (i <= 150):
	if(c == "Porto Velho") and (i <= 2):
		p= 0
		print("Passagem: R$",round(p,2))
	elif(c == "Porto Velho") and ((i == 3) or (i <= 12)):
		p= 500 * 0.50
		print("Passagem: R$",round(p,2))
	elif(c == "Porto Velho") and (( i > 12) and (i < 65)):
		p= 500.00
		print("Passagem: R$",round(p,2))
	elif(c == "Porto Velho") and (i >= 65 ):
		p= 500.00 * 0.70
		print("Passagem: R$",round(p,2))	
	elif (c == "Santarem") and( i <= 2):
		p=0
		print("Passsagem: R$",round(p,2))
	elif(c == "Santarem") and ((i == 3) or (i <= 12)):
		p= 370.00 * 0.50
		print("Passagem: R$",round(p,2))
	elif(c == "Santarem") and ((i > 12) and (i < 65)):
		p= 370.00
		print("Passagem: R$",round(p,2))
	elif(c == "Santarem") and (i > 65):
		p= 370.00 * 0.70
		print("Passagem: R$",round(p,2))
	elif(C == "Belem") and (i <= 2):
		p= 0
		print("Passagem: R$",round(p,2))
	elif(c == "Belem") and ((i == 3 ) or (i <= 12)):
		p= 600 * 0.50
		print("Passsagem: R$",round(p,2))
	elif(c == "Belem") and ((i > 12) and(i < 65)):
		p= 600
		print("Passagem: R$",round(p,2))
	elif(c == "Belem") and (i >= 65):
		p= 600 * 0.70
		print("Passagem: R$",round(p,2))
	elif(c == "Tefe") and (i <= 2):
		p=0
		print("Passagem: R$",round(p,2))
	elif(c == "Tefe") and ((i == 3) or (i <= 12)):
		p= 360 * 0.50
		print("Passagem: R$",round(p,2))
	elif(c == "Tefe") and ((i > 12) and (i < 65)):
		p= 360 
		print("Passagem: R$",round(p,2))
	elif(c == "Tefe") and (i >= 65):
		p= 360 * 0.70
		print("Passsagem: R$",round(p,2))
	elif(c == "Tabatinga")and(i <= 2):
		p=0
		print("Passsagem: R$",round(p,2))
	elif(c == "Tabatinga") and ((i==3) or (i <= 12)):
		p= 500.00 * 0.50
		print("Passagem: R$",round(p,2))
	elif(c == "Tabatinga") and ((i > 12) and (i < 65)):
		p= 550.00 
		print("Passagem: R$",round(p,2))
	elif(c == "Tabatinga") and (i >= 65):
		p= 550.00 * 0.70
		print("Passagem: R$",round(p,2))
else:
	print("entradas invalidas")
   