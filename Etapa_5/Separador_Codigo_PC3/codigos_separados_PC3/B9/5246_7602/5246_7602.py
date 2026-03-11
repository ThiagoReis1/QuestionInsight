idade = int(input("digite sua idade: "))
peso = float(input("digite seu peso"))

if idade >0 and idade <130:
	if peso >0 and peso <550:
		if idade <=20:
			if peso <=60:
				z = 9
				print ("Grupo de risco: ",round(z,1))
			elif peso>60 and peso <=90:
				z = 8
				print("Grupo de risco: ",round(z,1))
			else:
				z = 7
				print("Grupo de risco: ",round(z,1))
		elif idade>20 and idade <=50:
			if peso <=60:
				z = 6
				print("Grupo de risco: ",round(z,1))
			elif peso >60 and peso <=90:
				z = 5
				print("Grupo de risco: ",round(z,1))
			else:
				z=4
				print("Grupo de risco: ",round(z,1))
		else:
			if peso <=60:
				z = 3
				print("Grupo de risco: ",round(z,1))
			elif peso >60 and peso<=90:
				z = 2
				print("Grupo de risco: ",round(z,1))
			else:
				z=1
				print("Grupo de risco: ",round(z,1))
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")
			
			
			
	