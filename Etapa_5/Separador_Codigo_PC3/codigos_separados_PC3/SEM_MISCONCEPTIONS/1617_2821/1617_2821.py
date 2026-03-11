from numpy import*
espada = array(eval(input(""))) #vetor que indica o tipo de espada
inteiro = array(eval(input("")))
i = 0
while(i<size(espada)):
	if(espada[i] == "CENOURA"):
		d = 2*inteiro[i]
		i = i+1
	elif(espada[i]=="FERRO"):
		d = 4*inteiro[i]
   	i = i+1
	elif(espada[i]=="DWARVEN"):
		d = 8*inteiro[i]
		i = i+1
	elif(espada[i]=="ELVEN"):
		d = 11*inteiro[i]
		i = i+1
	elif(espada[i]=="DAEDRIC"):
		d = 14*inteiro[i]
		i = i + 1
print(d)

	
	
	