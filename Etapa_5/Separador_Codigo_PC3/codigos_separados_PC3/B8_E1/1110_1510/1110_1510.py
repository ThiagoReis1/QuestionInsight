#Universidade Federal do Amazonas
#Jorge Trajano da Silva Junior - 21553770
#Lab de configuração 03 - Avaliação parcial 3
#21/07/2016 - Exercício 1
#Solicitar entradas do usuário
p = int(input("Informe o número do prato: "))
s = int(input("Informe o número da sobremesa: "))
b = int(input("Informe o número da bebida: "))
#Condição de validade dos dados fornecidos
if(p >= 1 and p <= 4 and s >=1 and s <= 4 and b >= 1 and b <= 4):
	if(p == 1):
		prato = 180
	elif(p == 2):
		prato = 230
	elif(p == 3):
		prato = 250
	elif(p == 4):
		prato = 350
	if(s == 1):
		sobremesa = 75
	elif(s == 2):
		sobremesa = 110
	elif(s == 3):
		sobremesa = 170
	elif(s == 4):
		sobremesa = 200
	if(b == 1):
		bebida = 20
	elif(b == 2):
		bebida = 70
	elif(b == 3):
		bebida = 100
	elif(b == 4):
		bebida = 65
	cal = prato + sobremesa + bebida
	print("Entradas: ", p, ",",s,",",b)
	print("Calorias: ", cal, "cal")
else:
	print("Entradas: ", p, ",",s,",",b)
	print("Dados invalidos")