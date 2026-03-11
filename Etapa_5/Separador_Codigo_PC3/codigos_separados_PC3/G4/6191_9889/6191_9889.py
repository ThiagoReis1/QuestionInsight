l = input("Digite 'CARA' ou 'COROA': ").upper()

qdc = 0 #variavel contadora de cara

while (l!='S'):
	if (l == 'CARA'):
		qdc = qdc + 1
		
	l = input("Digite 'CARA' ou 'COROA': ").upper()
	
print(qdc)
		
			