i = int(input("Digite a sua idade: "))
p = float(input("Digite seu peso: "))

if(i>0 and i<=130 and p>0 and p<550):
	if(i<=20 and p<=60):
		g = "9"
		print("Entradas:", i, "anos", "e", p, "kg")
		print("Grupo de risco: ", g)
	elif(i<=20 and p>60 or p<=90):
		g = "8"
		print("Entradas:", i, "anos", "e", p, "kg")
		print("Grupo de risco:", g)	
	elif(i<=20 and p>90):
		g = "7"
		print("Entradas:", i, "anos e", p, "kg")
		print("Grupo de risco:", g)
	elif(i>20 or i<=50 and p<=60):
		g = "6"
		print("Entradas:", i, "anos", p, "kg")
		print("Grupo de risco:", g)
	elif(i>20 or i<=50 and p>60 or p<=90):
		g = "5"
		print("Entradas:", i, "anos","e", p, "kg")
		print("Grupo de risco:", g)
	elif(i>20 or i<=50 and p>90):
		g = "4"
		print("Entradas:",i,"anos e",p,"kg")
		print("Grupo de risco: ", g)
	elif(i>50 and p<=60):
		g = "3"
		print("Entradas:", i, "anos e", p, "kg")
		print("Grupo de risco: ", g)
	elif(i>50 and p>60 or p<=90):
		g = "2"
		print("Entradas:", i, "anos e",p,"kg")
		print("Grupo de risco: ", g)
	else:
		g = "1"
		print("Entradas:",i,"anos e",p,"kg")
		print("Grupo de risco:", g)
else:
	print("Entradas:",i,"anos e",p,"kg")
	print("Dados invalidos")