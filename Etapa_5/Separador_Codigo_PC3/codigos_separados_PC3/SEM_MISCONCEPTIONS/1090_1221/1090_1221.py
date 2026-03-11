c1=float(input("Digite o valor da compra: "))
c2=float(input("Digite o valor da compra: "))
c3=float(input("Digite o valor da compra: "))
c4=float(input("Digite o valor da compra: "))
limite=float(input("Limite da compra: "))
total=c1 + c2 + c3 + c4
if(total <= limite):
	print(round(total,2))
	print("Sim")
else:
	print(round(total,2))
	print("Nao")
