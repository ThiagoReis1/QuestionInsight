x = int(input("Ano de nascimento: "))
y = input("Pais: ").upper()

x1a = 2023 - x

if(x <= 2005) and (y == "B"):
	print("sim")
	print(x1a - 18)
	
elif(x <= 2006) and (y == "I"):
	print("sim")
	print(x1b - 17)
	
elif(x > 2005) and (y == "B"):
	print("nao")
	print(18 - x1a)
	
elif(x > 2006) and (y == "I"):
	print("nao")
	print(17-x1a)
	
else:
	print("invalido")
