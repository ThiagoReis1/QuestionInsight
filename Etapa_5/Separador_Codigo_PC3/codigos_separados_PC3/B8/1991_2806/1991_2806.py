var=input("Digite: ").upper()


o= 15.9994
c= 12.011
n= 14.00674
h= 1.0079

if(var == "GLICINA" or var == "PROLINA" or var == "SERINA"):
	if(var == "GLICINA"):
		glicina= round(((c*2) + (h*5) + (n*1) + (o*2)),2)
		print(glicina)
	
	elif(var == "PROLINA"):
		prolina= round(((c*5) + (h*10) + (n*1) + (o*2)),2)
		print(prolina)
		
	elif(var == "SERINA"):
		serina= round(((c*3) + (h*7) + (n*1) + (o*3)),2)
		print(serina)
		
else:
	print("Entrada:", var)
	print("Dado Invalido")