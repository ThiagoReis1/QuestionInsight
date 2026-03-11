at = input("Informe o ataque: ")

d1 = int(input("informe o valor do dado: "))
d2 = int(input("informe o valor do dado: "))
d3 = int(input("informe o valor do dado: "))
d4 = int(input("informe o valor do dado: "))

di = d1 + d2 + d3 + d4
			
if(at == "espada " ):
 print(di - 4 * 1 + 6)
	
else:
	print((d1 + d2 + d3) * d4)
	