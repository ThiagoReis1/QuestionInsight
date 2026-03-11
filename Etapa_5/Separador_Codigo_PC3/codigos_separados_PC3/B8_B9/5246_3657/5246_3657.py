idade=int(input(" "))
peso=float(input(" "))
if((idade>130 or idade<0) or (peso<0 or peso>550.0)):
	print("Entradas:",idade,"anos","e",round(peso,1),"kg")
	print("Dados invalidos")
elif(peso<=60):
	if(idade<=20):
		print("Entradas:", idade, "anos", "e", round(peso,1), "kg")
		print("Grupo de risco:", 9)
	elif(idade>20 and idade<=50):
		print("Entradas:", idade, "anos","e", round(peso,1), "kg")
		print("Grupo de risco:",6)
	elif(idade>50):
		print("Entradas:",idade,"anos","e",round(peso,1),"kg")
		print("Grupo de risco:",3)
elif(peso>60 and peso<=90 ):
	if(idade<=20):
		print("Entradas:", idade, "anos","e", round(peso,1), "kg")
		print("Grupo de risco:", 8)
	elif(idade>20 and idade<=50):
		print("Entradas:",idade,"anos","e",round(peso,1),"kg")
		print("Grupo de risco:",5)
	elif(idade>50):
		print("Entradas:",idade,"anos","e",round(peso,1),"kg")
		print("Grupo de risco:",2)
elif(peso>90):
	if(idade<=20):
		print("Entradas:",idade,"anos","e",round(peso,1),"kg")
		print("Grupo de risco:",7)
	elif(idade>20 and idade<=50):
		print("Entradas:",idade,"anos","e",round(peso,1),"kg")
		print("Grupo de risco",4)
	elif(idade>50):
		print("Entradas:",idade,"anos","e",round(peso,1),"kg")
		print("Grupo de risco",1)
	
		
		
		
	
		
	