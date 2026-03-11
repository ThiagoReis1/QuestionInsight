v = input("Digite a resposta:").upper()

cont = 0

while v != 'S':
	if v == 'SIM':
		cont = cont + 1
	v = input("Digite a respostu:").upper()
	
print(cont)