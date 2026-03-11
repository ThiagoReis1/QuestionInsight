ida = int(input("idade: "))
pes = float(input("peso: "))

if(ida <= 0) or (ida >= 130) or (pes <= 0.0) or (pes >= 550.0):
	print("Dados invalidos")
elif((ida<=20) and (pes<=60)):
	print("Entradas:", ida, "anos", "e", pes, "kg")
	print("Grupo de risco: 9 ")
elif((ida<=20) and (60<pes<=90)):
	print("Entradas:", ida, "anos", "e", pes, "kg")
	print("Grupo de rico: 8 ")
elif((ida<=20) and (pes>90)):
	print("Entradas:", ida, "anos", "e", pes, "kg")
	print("Grupo de risco: 7 ")
elif((20<ida<=50) and (pes<=60)):
	print("Entradas:", ida, "anos", "e", pes, "kg")
	print("Grupo de risco: 6 ")
elif((20<ida<=50) and (60<pes<=90)):
	print("Entradas:", ida, "anos", "e", pes, "kg")
	print("Grupo de risco: 5 ")
elif((20<ida<=50)and(pes>90)):
	print("Entradas:", ida, "anos", "e", pes, "kg")	
	print("Grupo de risco: 4 ")
elif((ida>50) and (pes<=60)):
	print("Entradas:", ida, "anos", "e", pes, "kg")
	print("Grupo de risco: 3 ")
elif((ida>50) and (60<pes<=90)):
	print("Entradas:", ida, "anos", "e", pes, "kg")
	print("Grupo de riso: 2 ")
else:
	print("Entradas:", ida, "anos", "e", pes, "kg"),
	print("Grupo de risco: 1 ")
							
		
	
	
	
	