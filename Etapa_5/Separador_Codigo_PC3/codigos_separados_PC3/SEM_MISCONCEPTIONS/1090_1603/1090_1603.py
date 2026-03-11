
compra1 = float(input("Qual o valor da primeira compra: "))
compra2 = float(input("Qual o valor da segunda compra: "))
compra3 = float(input("Qual o valor da terceira compra: "))
compra4 = float(input("Qual o valor da quarta compra: "))
limite_do_cartao = float(input("Qual o limite do cartao: "))

valor_total = compra1 + compra2 + compra3 + compra4

print(round(valor_total, 2))

if(valor_total <= limite_do_cartao):
	print("Sim")
else:
	print("Nao")