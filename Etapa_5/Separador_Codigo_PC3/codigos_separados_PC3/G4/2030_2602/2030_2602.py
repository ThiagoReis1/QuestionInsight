l = input("Dgite o lancamento: ").upper()
q = 0
while (l != "S".upper()):
	if (l == "CARA".upper()):
		q = q + 1
	l = input("Digite o lancamento: ").upper()
print (q)	
	