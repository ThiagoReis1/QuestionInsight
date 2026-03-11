x = int(input("Qual a sua idade?: "))
y = float(input("Qual o seu peso?: "))
print("Entradas:", x ,"anos e" , y ,"kg")
if( 0 < x < 130 and 0 < y < 550):
	if(x <= 20) and (y <= 60):
		print("Grupo de risco: 9")
	elif(x <= 20) and (60 < y <90):
		print("Grupo de risco: 8")
	elif(x <= 20) and (y > 90 ):
		print("Grupo de risco: 7")
	elif(20 < x <= 50) and (y <= 60):
		print("Grupo de risco: 6")
	elif(20 < x <= 50) and (60 < y <90):
		print("Grupo de risco: 5")
	elif(20 < x <= 50) and (y > 90):
		print("Grupo de risco: 4")
	elif(x > 50) and (y <= 60):
		print("Grupo de risco: 3")
	elif(x > 50) and (60 < y <90):
		print("Grupo de risco: 2")
	elif(x > 50) and (y > 90):
		print("Grupo de risco: 1")	
	else:
		print("Grupo de risco: Z")
else:
	print("Dados invalidos")