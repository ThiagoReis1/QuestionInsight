c1 = float(input("compra 1: "))
c2 = float(input("compra 2: "))
c3 = float(input("compra 3: "))
limite = float(input("limite do cartao: "))
valor = (c1 + c2 + c3)
print(round(valor, 2))

if (valor <= limite):
	print(" Nao ultrapassou ")
	
else: 
	print(" Ultrapassou ")