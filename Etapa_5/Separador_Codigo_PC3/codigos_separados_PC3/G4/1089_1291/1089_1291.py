c3 = float(input("digite o valor da primeira compra"))
c2 = float(input("digite o valor da segunda compra"))
c1 = float(input("digite o valor da terceira compra"))
limite = float(input("digite o valor do limite"))
calc = c1 + c2 + c3

print(round(calc,2))

if(calc <= limite):
	print ("Sim")
	
else:
	print ("Nao")
	
	
	

