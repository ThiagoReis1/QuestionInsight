r = input("").upper()
cont = 0
while (r.lower() != "s"):
	if ( r.upper() == "SIM"):
		mensagem = "SIM"
		cont= cont + 1
	else:
		mensagem = "NAO"

	r = input("")
print(cont)