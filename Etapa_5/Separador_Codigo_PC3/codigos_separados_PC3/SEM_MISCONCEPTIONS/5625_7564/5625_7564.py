opcao = input("Digite o pedido: ")
qua = int(input("Digite a quantidade: "))
acai = int(input("Digite a quantidade de acai: "))
tapi = 5.50
sagua = 4.00
pacai = 10.00
if(opcao.upper()=="S"):
	val = qua*sagua+acai*pacai
	print(val)
else:
	val = qua*tapi+acai*pacai
	print(val)
	