a = float(input("valor da compra 1: "))
b = float(input("valor da compra 2: "))
c = float(input("valor da compra 3: "))
l = float(input("digite o valor do limite: "))
valortotal = round((a + b + c),2)
if(valortotal <= l):
	print(valortotal)
	print("Sim")
else:
	print(valortotal)	
	print("Nao")	
	