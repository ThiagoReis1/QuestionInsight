compra1=float(input("Informe o valor da primeira compra: "))
compra2=float(input("Informe o valor da segunda compra: "))
compra3=float(input("Informe o valor da terceira compra: "))
compra4=float(input("Informe o valor da quarta compra: "))
limite=float(input("Informe o limite do seu cartao: "))
t=round(compra1+compra2+compra3+compra4,2)
l=round(limite,2)
if l==t or l>=t:
	print(t)
	print("Sim")
else:
	print(t)
	print("Nao")