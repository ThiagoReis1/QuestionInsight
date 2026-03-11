from numpy import *
faces= array(eval(input("")))
i = 0
cont = 100
while i < size(faces):
	if faces[i] == 2:
	    cont = cont * 2
	elif faces[i] == 3:
	   cont = cont / 3
	elif faces[i] == 4:
	   cont = cont * 4
	elif faces[i] == 5:
		cont = cont / 5
	elif faces[i] == 6:
		cont = cont * 6
	cont += 0
	i += 1
print(round(cont, 2))
    
	 
	

