ano= int(input("Digite o ano de nasc:"))
pais= input("B ou R:").upper()

conta= 2023 - ano

if pais == "B" or pais == "R":
	if pais == "B":
		if conta >= 18:
			
			print("sim")
			print(conta -18)
		else:
			print("nao")
			print(18-conta)
	else:
		if conta >= 21:
			print("sim")
			print(conta - 21)
		else:
			print("nao")
			print(21-conta)
else:
	print("invalido")
		
		