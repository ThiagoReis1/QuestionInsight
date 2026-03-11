e = input("Digite (PRETA / VERMELHA): ").upper()
acm = 1

while(e != "S" or e == "VERMELHA"):
	acm = acm - 1
	e = input("Digite (PRETA / VERMELHA):").upper()
	if(e == "PRETA"):
		acm = acm + 1
print(acm)