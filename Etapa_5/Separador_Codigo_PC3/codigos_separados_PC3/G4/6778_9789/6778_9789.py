ano = int(input("em qual ano voce nasceu:"))
P = input("pais:").upper()

idd = (2023) - ano 

if P == "B" and idd >= 21:
	print ("sim")
	apta = idd - 21
	print (apta)
	
elif P == "B" and idd < 21:
	print ("nao")
	apta = 21 - idd
	print (apta)
	
elif P == "J" and idd >= 20:
	print ("sim")
	apto = idd - 20
	print (apto)
	
elif P == "J" and idd < 20:
	print ("nao")
	apto = 20 - idd
	print (apto)
	
else:
	print("invalido")