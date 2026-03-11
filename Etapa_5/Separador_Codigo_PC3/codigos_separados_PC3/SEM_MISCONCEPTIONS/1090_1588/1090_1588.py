compra1 = float(input("Digite o valor 1:  "))
compra2 = float(input("Digite o valor 2:  "))
compra3 = float(input("Digite o valor 3:  "))
compra4 = float(input("Digite o valor 4:  "))
limite = float(input("Digite o limite do cartão:   "))

vt = (compra1 + compra2 + compra3 + compra4)

if(vt <= limite):
	mensagem = ("Sim")
	print(round(vt,2))
	print(mensagem)
else:
	mensagem = ("Nao")
	print(round(vt,2))
	print(mensagem)