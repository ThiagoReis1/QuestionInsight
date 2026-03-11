i=int(input("idade: "))
p=float(input("peso: "))
print("Entradas: ", i, "anos e ", round(p,1), "kg")
if(((i< 0)or(i>130)) or ((p<0) or (p>550))):
	print("Dados invalidos")
elif(i<=20):
	if(p<=60):
		print("Grupo de risco: 9")
	else:
		if((p>60) and (p<=90)):
			print("Grupo de risco: 8")
		else:
				print("Grupo de risco: 7")
elif((i>20) and (i<=50)):
	if(p<=60):
		print("Grupo de risco: 6")
	else:
		if((p>60) and (p<=90)):
			print("Grupo de risco: 5")
		else:
			print("Grupo de risco: 4")
elif(i>50):
	if(p<=60):
		print("Grupo de risco: 3")
	else:
		if((p>60) and (p<=90)):
			print("Grupo de risco: 2")
		else:
			print("Grupo de risco: 1")
	
