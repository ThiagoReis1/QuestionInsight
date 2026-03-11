n = int(input("n: "))

cont = 0
contt = 0
conte = 0
conta = 0


while cont < n:
	prof = input("escolha: ").lower
	
	if(prof == "tais"):
		contt = cont + 1
		
	elif(prof == "edgar"):
		conte = cont + 1
		
	elif(prof == "ana"):
		conta = cont + 1
		
	else:
		cont = cont + 1
print("tais= ", contt)
print("edgar= ", conte)
print("ana= ", conta)
	







