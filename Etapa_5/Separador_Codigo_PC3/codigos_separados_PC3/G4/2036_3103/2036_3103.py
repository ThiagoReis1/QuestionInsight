cor = input("Qual a cor da bolinha?: ").upper()
Qp = 0
while(cor != "S"):
	if(cor == "PRETA"):
		Qp = Qp + 1
		cor = input("Qual a cor da bolinha?: ").upper()
	else:
		cor = input("Qual a cor da bolinha?: ").upper()
print(Qp)		
		
	