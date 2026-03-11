x = int(input("Digite a idade: "))
y = float(input("Digite o peso: "))
print("Entradas:",x,"anos","e",y,"kg")
if((0<x<=130) and (0<y<=550.0)):
	if(x<=20):
		if(y<=60):
			print("Grupo de risco: 9")
		elif(60<y<=90):
			print("Grupo de risco: 8")
		else:
			print("Grupo de risco: 7")
	elif(20<x<=50):
		if(y<=60):
			print("Grupo de risco: 6")
		elif(60<y<=90):
			print("Grupo de risco: 5")
		else:
			print("Grupo de risco: 4")
	elif(x>50):
		if(y<=60):
			print("Grupo de risco: 3")
		elif(60<y<=90):
			print("Grupo de risco: 2")
		else:
			print("Grupo 1")
else:
	print("Dados invalidos")
			