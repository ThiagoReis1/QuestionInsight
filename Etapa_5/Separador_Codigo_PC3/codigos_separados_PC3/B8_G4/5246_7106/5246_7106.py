ida = int(input("idade:  "))
pes = float(input("Peso:  "))

print("Entradas:", ida, "anos e", round(pes,1), "kg")

if (ida >=0 and ida<=130) and (pes >=0.0 and pes <=550.0):
	if ida <=20 and pes<=60:
		print("Grupo de risco: 9")
	elif ida <=20 and (pes>60 and pes<=90):
		print("Grupo de risco: 8")
	elif ida <=20 and pes>90:
		print("Grupo de risco: 7")
	elif (ida >20 and ida<=50) and pes <=60:
		print("Grupo de risco: 6")
	elif (ida>20 and ida<=50) and (pes>60 and pes<=90):
		print("Grupo de risco: 5")
	elif (ida>20 and ida<=50) and pes>90:
		print("Grupo de risco: 4")
	elif ida>50 and pes <=60:
		print("Grupo de risco: 3")
	elif ida>50 and (pes>60 and pes<=90):
		print("Grupo de risco: 2")
	elif ida>50 and pes>90:
		print("Grupo de risco: 1")
else:
	print("Dados invalidos")
		
