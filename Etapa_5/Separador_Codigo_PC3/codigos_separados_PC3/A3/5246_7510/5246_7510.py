idade = int(input())
peso = float(input())


x = 0
if idade >=0 and idade <=130 and peso >=0 and peso<=550:
	if idade <=20:
		if peso <=60:
			x = 9
		elif(peso<=90):
			x = 8
		else:
			x = 7
	elif idade <=50:
		if peso <=60:
			x = 6
		elif peso<=90:
			x = 5
		else:
			x = 4
	else:
		if peso<=60:
			x = 3
		elif peso<=90:
			x = 2
		else:
			x = 1

if x == 0:
	print("Dados invalidos")
else:
	print("Grupo de risco: ",x)
			