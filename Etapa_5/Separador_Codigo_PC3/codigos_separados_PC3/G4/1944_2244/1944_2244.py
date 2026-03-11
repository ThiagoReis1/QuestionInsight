nome= input("Qual o nome do aminoacido:")

if(nome.lower() == "leucina"):
	peso= float(12.011*6) + (1.0079*13) + (14.00674) + (15.9994*2)
	print(round(peso,2))

else:
	peso= float(12.011*6) + (1.0079*15) + (14.00674*2) + (15.9994*2)
	print(round(peso,2))