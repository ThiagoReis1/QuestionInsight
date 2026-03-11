I=int(input("insira a idade:"))
P=float(input("Insira o peso:"))
if ((I<=0) or (I>=130) or (P<=0.0) or (P>=550.0)):
	print ("Entradas:",I,"anos e",P,"kg")
	print ("Dados invalidos")
elif ((0<I<=20) and (0<P<=60)):
	k=9
	print ("Entradas:",I,"anos e",P,"kg")
	print ("Grupo de risco:",k)
elif ((0<I<=20) and (60<P<=90)):
	k=8
	print ("Entradas:",I,"anos e",P,"kg")
	print ("Grupo de risco:",k)
elif ((0<I<=20) and (P>90)):
	k=7
	print ("Entradas:",I,"anos e",P,"kg")
	print ("Grupo de risco:",k)
elif ((20>I>=50) and (0<P<=60)):
	k=6
	print ("Entradas:",I,"anos e",P,"kg")
	print ("Grupo de risco:",k)
elif ((20>I>=50) and (60<P<=90)):
	k=5
	print ("Entradas:",I,"anos e",P,"kg")
	print ("Grupo de risco:",k)
elif ((20>I>=50) and (P>90)):
	k=4
	print ("Entradas:",I,"anos e",P,"kg")
	print ("Grupo de risco:",k)
elif ((I>50) and (0>P>=60)):
	k=3
	print ("Entradas:",I,"anos e",P,"kg")
	print ("Grupo de risco:",k)
elif ((I>50) and (60<P<=90)):
	k=2
	print ("Entradas:",I,"anos e",P,"kg")
	print ("Grupo de risco:",k)
elif	((I>50) and (P>90)):
	k=1
	print ("Entradas:",I,"anos e",P,"kg")
	print ("Grupo de risco:",k)