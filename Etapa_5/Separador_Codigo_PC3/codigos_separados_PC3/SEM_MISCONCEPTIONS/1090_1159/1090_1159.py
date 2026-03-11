valor1=round(float(input("digite o valor da compra")),2)
valor2=round(float(input("digite o valor da compra")),2)
valor3=round(float(input("digite o valor da compra")),2)
valor4=round(float(input("digite o valor da compra")),2)
valor_total=round((valor1+valor2+valor3+valor4),2)
limite=round(float(input("digite o valor do limite")),2)
if (valor_total <= limite):
	print(valor_total)
	print("Sim")
else:
	print(valor_total)
	print("Nao")