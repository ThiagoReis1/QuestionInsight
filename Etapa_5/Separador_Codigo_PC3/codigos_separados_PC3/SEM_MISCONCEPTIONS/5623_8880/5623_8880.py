pedido = input("s ou b : ").upper()
q= int(input("infome a quantidade de bolo ou salgados: "))
c= int(input("informe a quantidade de cappucino: "))

if pedido== "S":

   preco = q* 4 + (c*7.50)
   print(round(preco,2))

else :
	
	preco= q *5 + (c*7.50)
	print(round(preco,2))
	
	

	
	
