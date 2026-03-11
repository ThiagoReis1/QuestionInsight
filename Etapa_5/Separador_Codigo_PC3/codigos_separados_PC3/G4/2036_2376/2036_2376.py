#Valores iniciais 
x = input("PRETA ou VERMELHA?: ").upper()

#Variavel contadora
p = 0

#Laco de acumulacao
while (x != "S"):
	if (x == "PRETA"):
		p = p + 1
	x = input("PRETA ou VERMELHA?: ").upper()
	

print(p)