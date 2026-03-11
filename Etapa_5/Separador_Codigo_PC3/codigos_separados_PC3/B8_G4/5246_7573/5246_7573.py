idd = int(input("Digite a idade: "))
ps = float(input("Digite o peso: "))

if(idd < 0 or idd > 130 or ps < 0.0 or ps > 550.0):
	print("Dados invalidos")
else:
	if (idd > 50 and ps <= 60.0):
		print("Grupo de risco: 3")
	elif(idd > 50 or ps > 60.0 or ps < 90.0):
		print("Grupo de risco: 2")
	elif(idd > 50 and ps >= 90.0):
		print("Grupo de risco: 1")
	elif(idd > 20 or idd < 50 and ps <= 60.0):
		print("Grupo de risco: 9")
	elif(idd > 20 or idd < 50 or ps > 60.0 or ps <90.0):
		print("Grupo de risco: 8")
		