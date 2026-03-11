dado = int(input("digite o numero do dado: "))

#acumular o numero de dados = 6
acumu = 0

while(dado != -1):
	if(dado == 6):
		acumu = acumu + 1 
	dado = int(input("digite o numero do dado: "))
	
print(acumu)
