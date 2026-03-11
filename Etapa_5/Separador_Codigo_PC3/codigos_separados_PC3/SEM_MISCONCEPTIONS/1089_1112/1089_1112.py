a = float(input("Digite o Valor da compra1:"))
b = float(input("Digite o Valor da compra2:"))
c = float(input("Digite o Valor da compra3:"))
total = a+b+c
limite =float(input("Digite o limite:"))
print(round(total,2))
if (total<=limite):
	 print("Sim")
else:
	 print("Nao")