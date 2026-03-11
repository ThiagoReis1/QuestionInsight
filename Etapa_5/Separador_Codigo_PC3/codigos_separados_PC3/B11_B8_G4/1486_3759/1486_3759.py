nome = input("Digite aqui o ingrediente:") 
q = int(input("Digite aqui a quantidade do ingretiente:"))

if(q < 0 or q > 10000):
	print("Entrada invalida")
else:	
	if(nome.upper() == "ARROZ"):
		c = q / 500
		print(int(c))
	if(nome.upper() == "CENOURA"):
		c = q / 100
		print(int(c))
	if(nome.upper() == "KAMPYO"):
		c = q / 20
		print(int(c))
	if(nome.upper() == "NORI"):
		c = q / 50
		print(int(c))
	if(nome.upper() == "OMELETE"):
		c = q / 200
		print(int(c))
	if(nome.upper() == "PEPINO"):
		c = q / 150
		print(int(c))
	if(nome.upper() == "SALMAO"):
		c = q / 300
		print(int(c))
	if(nome.upper() == "SHITAKE"):
		c = q / 150
		print(int(c))