# Instituto de Computacao -UFAM
# Avaliacao 3 
# 15 / 06 / 2016
#-----------------------------------------------------
X= float(input("digite o preço normal da entrada: "))
Y= int(input("digite o dia da semana: "))
Z= input("É dia de música ao vivo? ('S' ou 'N')")
if (X>= 0 and Y>=1 and Y<=7) and (Z== "S" or Z== "N"):
	if(X>=0 and Y==1 and Z=="S" or Z=="N"):
		W= X-(X*0.25)
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==1 and z=="S"):
		W = X+20.00
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==2 and Z=="N"):
		W= X-(X*0.25)
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==2 and Z=="S"):
		W = X+20.00
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==3 and Z=="N"):
		W= X-(X*0.25)
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==3 and Z=="S"):
		W = X+20.00
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==4 and Z=="N"):
		W= X-(X*0.25)
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==4 and Z=="S"):
		W = X+20.00
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==5 and Z=="N"):
		W= X-(X*0.25)
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==5 and Z=="S"):
		W = X+20.00
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==6 and Z=="N"):
		W= X-(X*0.25)
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==6 and Z=="S"):
		W = X+20.00
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==7 and Z=="N"):
		W= X-(X*0.25)
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
	elif (X>=0 and Y==7 and Z=="S"):
		W = X+20.00
		W= round(W,2)
		print("Entradas:", X, ",", Y, ",", Z)
		print("valor a pagar: R$", W)
else:
	print("Entradas:", X, ",", Y, ",", Z)
	print("Dados invalidos")