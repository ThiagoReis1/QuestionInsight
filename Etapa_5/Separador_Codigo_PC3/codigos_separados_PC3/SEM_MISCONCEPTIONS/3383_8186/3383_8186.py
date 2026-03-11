medida = input("qual a medida usada?: ").upper()
valor = float(input("qual a unidade usada?: "))

if medida == "L":
	conta = valor/2.20462
	print(round(conta, 2))
	
else: 
	conta = 2.20462*valor
	print(round(conta, 2))
				  
