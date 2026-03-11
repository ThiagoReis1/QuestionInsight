num = int(input("digite um numero inteiro: "))
pais = input("digite B ou E: ").upper()


idade = 2023 - num
if pais == "B":
	if idade > 17:
		conta = idade - 18
		print("sim")
		print(conta)
	else:
		conta = 18 - idade
		print("nao")
		print(conta)
elif pais == "E":
	if idade > 15:
		conta = idade - 16
		print("sim")
		print(conta)
	else:	
		conta = 16 - idade
		print("nao")
		print(conta)
else:
	print("invalido")
				
	
	
	
	
		
	
	

