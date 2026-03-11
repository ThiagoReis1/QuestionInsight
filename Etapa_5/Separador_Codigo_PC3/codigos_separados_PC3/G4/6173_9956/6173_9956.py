resp = input("digite sua resposta").upper()
cont = 0

while resp != 'S':
	if resp == 'SIM':
		cont = cont + 1
	resp = input("digite sua resposta").upper()
	
print (cont)