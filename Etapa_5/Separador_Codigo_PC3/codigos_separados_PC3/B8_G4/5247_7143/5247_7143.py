sa = float(input("digite o salario atual: "))
co = int(input("digite o codigo correspondente ao cargo do funcionario:"))

print("Entradas: R$", sa, "e codigo", co)

if(co == 101 or co == 102 or co == 103 or co == 104):
	if(co == 101):
		t =  (sa + (sa*0.008))
		print("Novo salario: R$" , round(t , 2))
	elif(co == 102):
		x = (sa + (sa*0.0065))
		print("Novo salario: R$", round (x, 2))
	elif(co == 103):
		y = (sa + (sa*0.006))
		print("Novo salario: R$", round (y , 2))
	elif (co == 104):
		w = (sa + (sa*0.0055))
		print ("Novo salario: R$", round( w, 2))
else:
	print("Dados invalidos")
		