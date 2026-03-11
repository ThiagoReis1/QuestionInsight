face = int(input("Qual a face sorteada?"))
			  
cont = 0
cont_6 = 0

while face != -1:
	if face == 6:
		cont = cont + 1
		cont_6 = cont_6 + 1
	else:
		cont = cont + 1
		cont_6 = cont_6
	face = int(input("Qual a face sorteada?"))		  

porc = (cont_6/cont)*100
print(cont)
print(round(porc,2))			  