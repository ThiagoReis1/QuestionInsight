r = input("respostas: ").upper()

cont = 0
cont2 = 0

while(r!="S"):
	if(r=="SIM"):
		cont2 = cont2 + 1
		cont = cont + 1
	elif(r=="NAO"):
		cont2 = cont2 + 1
		cont = cont + 0
	r = input("respostas: ").upper()
	
print(round(cont2))
print(round(cont/cont2*100,2))
