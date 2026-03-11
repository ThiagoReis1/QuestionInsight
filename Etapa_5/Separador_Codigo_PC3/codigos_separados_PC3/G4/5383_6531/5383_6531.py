from numpy import*
et = input("Etiquetas: ").upper()

i = 0
j = 0
k = 0
while(i < len(et)):
	if(et[i] == "A" or et[i] == "E" or et[i] == "I" or et[i] == "O" or et[i] == "U" ):
		j = j + 1
	else:
		k = k + 1
	i = i + 1
print(round(j*0.12+k*0.18, 2))
		
	  


