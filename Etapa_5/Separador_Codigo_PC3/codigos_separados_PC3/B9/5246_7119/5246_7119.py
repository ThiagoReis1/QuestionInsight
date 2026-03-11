idade=int(input())
peso=float(input())
print("Entradas:",idade,"anos e",round(peso,1),"kg")
if(idade>0 and idade<=130 and peso>=0 and peso<=550 ):
	if(idade<=20):
		if(peso<=60):
			mes="9"
		elif(peso>60 and peso <=90):
			mes="8"
		else:
			mes="7"
	elif(idade>20 and idade <=50):
		if(peso<=60):
			mes="6"
		elif(peso>60 and peso<=90):
			mes="5"
		else:
			mes="4"
	else:
		if(peso<=60):
			mes="3"
		elif(peso>60 and peso<=90):
			mes="2"
		else:
			mes="1"
	print("Grupo de risco:",mes)
else:
	print("Dados invalidos")