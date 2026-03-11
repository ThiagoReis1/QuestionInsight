#ex 1

idade = int(input("idade:"))
peso = float(input("peso:"))
print("Entradas:",idade, "anos e", peso,"kg")
if(0 > idade > 130) and (0.0 > peso > 550.0):
	print("Entradas:",idade, "anos e", peso,"kg")
	
if(idade <= 20) and (peso <= 60.0):
	print("grupo de risco: 9")
elif(20 < idade <= 50) and (peso <= 60.0):
	print("grupo de risco: 6")
elif(idade > 50) and (peso <= 60.0):
	print("grupo de risco: 3")
elif(idade <= 20) and (60.0 < peso <= 90.0):
	print("grupo de risco: 8")
elif(20 < idade <= 50) and (60.0 < peso <= 90.0):
	print("grupo de risco: 5")
elif(idade > 50) and (60.0 < peso <= 90.0):
	print("grupo de risco: 2")
elif(idade <= 20) and ( peso > 90.0):
	print("grupo de risco: 7")
elif(20 < idade <= 50) and ( peso > 90.0):
	print("grupo de risco: 4")
elif(idade > 50) and ( peso > 90.0):
	print("grupo de risco: 1")
else:
	print("Dados invalidos")
	
elif(idade > 50) and ( peso > 90.0):
	print("grupo de risco: 1")	
elif(idade > 50) and (60.0 < peso <= 90.0):
	print("grupo de risco: 2")
elif(idade > 50) and (peso <= 60.0):
	print("grupo de risco: 3")
elif(20 < idade <= 50) and ( peso > 90.0):
	print("grupo de risco: 4")
elif(20 < idade <= 50) and (60.0 < peso <= 90.0):
	print("grupo de risco: 5")
elif(20 < idade <= 50) and (peso <= 60.0):
	print("grupo de risco: 6")
