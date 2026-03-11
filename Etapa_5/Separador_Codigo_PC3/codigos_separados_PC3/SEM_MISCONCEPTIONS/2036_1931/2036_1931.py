bolinha = input("Digite a cor: ").upper()
q = 0
while(bolinha != "S"):
	if(bolinha == "PRETA"):
		q = q + 1
	bolinha = input("digite a cor: ").upper()
print(q)