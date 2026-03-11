ano = int(input("insira: "))
cb = input("insira: ").upper()

if(cb == "B"):
	if(2023-ano >17):
		print("sim")
		print(2023-(ano+18) )
	else:
		print("nao")
		print((2023-(ano+18))*-1)
		
elif(cb == "E"):
	if(2023-ano >15):
		print("sim")
		print(2023-(ano+16))
	else:
		print("nao")
		print((2023-(ano+16))*-1)
else:
	print("invalido")