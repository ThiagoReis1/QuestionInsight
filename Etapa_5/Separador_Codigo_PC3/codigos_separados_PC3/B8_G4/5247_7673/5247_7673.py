a = float(input())
cod = int(input())

if(a > 0) and (cod == 101):
	r = 0.80
	salario = a + (r/100) * a
	print("Novo salario: R$", round(salario, 2))
elif(a > 0) and (cod == 102):
	r = 0.65
	salario = a + (r/100) * a
	print("Novo salario: R$", round(salario, 2))
elif(a > 0) and (cod == 103):
	r = 0.60
	salario = a + (r/100) * a 
	print("Novo salario: R$", round(salario, 2))
elif(a > 0) and (cod == 104):
	r = 0.55
	salario = a + (r/100) * a 
	print("Novo salario: R$", round(salario, 2))
else:
	 if(a <=0) or (cod != 101) or (cod != 102) or (cod != 103) or (cod != 104): 
	   print("Dados invalidos")


		

	
	
	