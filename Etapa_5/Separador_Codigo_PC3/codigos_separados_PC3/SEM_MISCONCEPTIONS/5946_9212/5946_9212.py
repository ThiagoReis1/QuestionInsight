a = input("L se for lanche ou P se for pizza:")
quantidade = int(input("informe a quantidade:"))
quantidade_refri = int(input("informe a quantidade de refrigerante:"))

if a.upper() == "L":
	valor = quantidade * 6 + quantidade_refri * 3.0

else:
	valor = quantidade* 4.50 + quantidade_refri*3.0
	
print(round(valor,2))