x=int(input("Qual a idade: "))
y=float(input("Qual o peso: "))
if((x<0)or(x>130)or(y<0)or(y>550)):
	print("Entradas:",x,"anos e",y,"kg") 
	print("Dados invalidos")
elif((x<=20)and(y<=60)):
	print("Entradas:",x,"anos e",y,"kg")
	print("Grupo de risco: 9")
elif((x<=20)and(60<y<=90)):
	print("Entradas:",x,"anos e",y,"kg")
	print("Grupo de risco: 8")
elif((x<=20)and(90<y)):
	print("Entradas:",x,"anos e",y,"kg")
	print("Grupo de risco: 7")
elif((120<x<=50)and(y<=60)):
	print("Entradas:",x,"anos e",y,"kg")
	print("Grupo de risco: 6")
elif((120<x<=50)and(60<y<=90)):
	print("Entradas:",x,"anos e",y,"kg")
	print("Grupo de risco: 5")
elif((120<x<=50)and(90<y)):
	print("Entradas:",x,"anos e",y,"kg")
	print("Grupo de risco: 4")
elif((x>50)and(y<=60)):
	print("Entradas:",x,"anos e",y,"kg")
	print("Grupo de risco: 3")
elif((x>50)and(60<y<=90)):
	print("Entradas:",x,"anos e",y,"kg")
	print("Grupo de risco: 2")
elif((x>50)and(90<y)):
	print("Entradas:",x,"anos e",y,"kg")
	print("Grupo de risco: 1")
