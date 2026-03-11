i = int(input("Digite a idade: "))
p = float(input("Digite o peso: "))
if (0<=i<=130) and (0.0<=p<=550.0):
	if (i<=20) and (p<=60):
		print("Grupo de risco: 9")
	elif (i<=20) and (60<p<90):
		print("Grupo de risco: 8")
	elif (i<=20) and (p>90):
		print("Grupo de risco: 7")
	elif (20<i<50) and (p<=60):
		print("Grupo de risco: 6")
	elif (20<i<50) and (60<p<90):
		print("Grupo de risco: 5")
	elif (20<i<50) and (p>90):
		print("Grupo de risco: 4")
	elif (i>50) and (p<=60):
		print("Grupo de risco: 3")
	elif (i>50) and (60<p<90):
		print("Grupo de risco: 2")
	elif (i>50) and (p>90):
		print("Grupo de risco: 1")
else:
	print("Dados invalidos")