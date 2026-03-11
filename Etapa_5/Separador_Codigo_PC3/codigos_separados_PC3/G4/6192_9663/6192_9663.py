v = input("Digite qual opcao voce deseja para v: ").upper()

cont= 0


while (v != "S"):
	if (v == "PRETA"):
		cont = cont + 1
		v = input("Digite qual opcao voce deseja para v: ").upper()
	else:
		v = input("Digite qual opcao voce deseja para v: ").upper()
print(cont)