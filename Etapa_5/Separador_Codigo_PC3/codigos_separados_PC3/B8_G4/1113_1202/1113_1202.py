x=float(input("Determine sua idade:"))
y=float(input("Determine seu peso:"))

print("Entradas:",x,"anos e",y,"kg")

#condiçao para as entradas serem validas
if((x>=0 or x<=130) and (y>=0 or y<=550.0)):
	if(x>50 and y>90):
		print("Grupo de risco: 1")
	elif(x>50 and y>60 or y<=90):
		print("grupo de risco: 2")
	elif(x>50 and y<=60):
		print("Grupo de risco: 3")
	elif((x>20 or x<=50) and y>90):
		print("Grupo de risco: 4")
	elif((x>20 or x<=50) and (y>60 or y<=90)):
		print("Grupo de risco: 5")
	elif(x>20 or (x<=50 and y<=60)):
		print("Grupo de risco: 6")
	elif(x<=20 and y>90):
		print("Grupo de risco: 7")
	elif(x<=20 and (y>60 or y<=90)):
		print("Grupo de risco: 8")
	elif(x<=20 and y<=60):
		print("Grupo de risco: 9")
else:
	print("Dados: invalidos")
		
		
		
		
		
		
		
		
	