# faça seu código aqui!
tipo = input("A, B ou C: ").upper()
qnt = int(input("quantidade: "))
l = 30

if tipo == "B":
	valor = qnt * l
	
if tipo == "C":
	des = (qnt * l) * (15/100)
	valor = (qnt * l) - des

else:
	valor = qnt * l
	
print(round(valor, 2))
