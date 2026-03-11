i = int(input())
p = float(input())
if (i > 0) and (i < 130) and (p > 0) and (p < 550.0):
	if (i <= 20) and (p <= 60):
		print("Grupo de risco: 9")
	elif (i <= 20) and (p > 60) and (p <= 90):
		print("Grupo de risco: 8")
	elif (i <= 20) and (p > 90):
		print("Grupo de risco: 7")
	elif (i > 20) and (i <= 50) and (p <= 60):
		print("Grupo de risco: 6")
	elif (i > 20) and (i <= 50) and (p > 60) and (p <= 90):
		print("Grupo de risco: 5")
	elif (i > 20) and (i <= 50) and (p > 90):
		print("Grupo de risco: 4")
	elif (i > 50) and (p <= 60):
		print("Grupo de risco: 3")
	elif (i > 50) and (p > 60) and (p <=90):
		print("Grupo de risco: 2")
	elif (i > 50) and (p > 90):
		print("Grupo de risco: 1")
else:
	print("Dados invalidos")