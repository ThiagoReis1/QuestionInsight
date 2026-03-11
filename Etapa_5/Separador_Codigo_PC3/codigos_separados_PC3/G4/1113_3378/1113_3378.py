i=int(input("idade: "))
p=float(input("peso: "))

print("Entrada: ",i, "anos e ",p,"kg")

if (i>0 and i<=20) or (i>20 and i<=50) or (i>50):
	if (i>0 and i<=20):
		if (0<=p and p<=60):
			print("Grupo de risco: 9")
		elif (p>60 and p<=90):
			print("Grupo de risco: 8")
		else:
			print("Grupo de risco: 7")
	if (i>20 and i<=50):
		if (0<=p and p<=60):
			print("Grupo de risco: 6")
		elif (p>60 and p<=90):
			print("Grupo de risco: 5")
		else:
			print("Grupo de risco: 4")
	if (i>50):
		if (0<=p and p<=60):
			print("Grupo de risco: 3")
		elif (p>60 and p<=90):
			print("Grupo de risco: 2")
		else:
			print ("Grupo de risco: 1")
else:
	print("Dados invalidos")
			