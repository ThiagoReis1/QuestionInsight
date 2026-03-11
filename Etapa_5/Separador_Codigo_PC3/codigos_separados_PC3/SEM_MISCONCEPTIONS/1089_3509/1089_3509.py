comp1 = float(input("compra 1:"))
comp2 = float(input("compra 2:"))
comp3 = float(input("compra 3:"))
limite = float(input("limite do cartao:"))
vtotal =(comp1 + comp2 + comp3)
if(vtotal <= limite):
	print(round(vtotal,2))
	print("Nao ultrapassou")
else :
	print(round(vtotal,2))
	print("Ultrapassou")


