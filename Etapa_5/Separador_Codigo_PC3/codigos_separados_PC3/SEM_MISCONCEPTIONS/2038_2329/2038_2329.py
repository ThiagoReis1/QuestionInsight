resposta = input("informe a resposta do cliente: ").upper()
qc = 0
while(resposta != "S"):
	if(resposta == "SIM"):
		resposta = input("informe a resposta do cliente: ")
		qc = qc + 1
	else:
		resposta = input("informe a resposta do cliente: ")
print(qc)
