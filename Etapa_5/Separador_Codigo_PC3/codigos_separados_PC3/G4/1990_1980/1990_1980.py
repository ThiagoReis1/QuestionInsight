ent = input("")

if(ent.upper() == "GLUTAMINA"):
	
	peso = float((12.011 * 5) + (1.00794 * 8) + (14.0067) + (15.9994 * 4))
	print(round(peso,2))

elif(ent.upper() == "SERINA"):
	
	peso = float((12.011 * 3) + (1.00794 * 7) + (14.0067 + (15.9994 * 3)))
	print(round(peso,2))
			
elif(ent.upper() == "TREONINA"):
	
	peso = float((12.011 * 4) + (1.00794 * 9) + (14.0067 + (15.9994 * 3)))
	print(round(peso,2))
			
else:
	
	print("Entrada:",ent)
	print("Dado Invalido")
	
