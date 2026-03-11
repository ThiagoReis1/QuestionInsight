i = int(input("idade: "))
p = float(input("peso: "))

if((i>=0 and i<=130 ) and (p>=0.0 and p<=550.0)):
	print("Entradas:",round(i,1) , "anos e" , round(p,1),"kg")
	if(i<=20):
		if(p<=60):
			print("Grupo de risco: 9")
		if(p>60 and p<= 90):
			print("Grupo de risco: 8")
		if(p>=90):
			print("Grupo de risco: 7")
	if(i>20 and i<=50):
		if(p<=60):
			print("Grupo de risco: 6")
		if(p>60 and p<= 90):
			print("Grupo de risco: 5")
		if(p>=90):
			print("Grupo de risco: 4")
	if(i>50):
		if(p<=60):
			print("Grupo de risco: 3")
		if(p>60 and p<= 90):
			print("Grupo de risco: 2")
		if(p>=90):
			print("Grupo de risco: 1")		
else:
	print("Entradas:",round(i,1) , "anos e" , round(p,1) ,"kg")
	print("Dados invalidos")