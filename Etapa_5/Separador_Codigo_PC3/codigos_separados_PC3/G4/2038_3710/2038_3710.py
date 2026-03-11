x = input("Insira Sim ou Nao: ")
cont = 0

while(x.upper() != 'S'):
	if(x.upper() == 'SIM'):
		cont = cont + 1
		x = input("Insira Sim ou Nao: ")
	else:
		x = input("Insira Sim ou Nao: ")
print(cont)