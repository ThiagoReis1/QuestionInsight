resp = input("Digite resposta do cliente: ").upper()

ac = 0

while(resp != "S"):
	if(resp == "SIM"):
		ac = ac + 1
	elif(resp == "NAO"):
		ac = ac + 0
	resp = input("Digite resposta do cliente: ").upper()
print(ac)