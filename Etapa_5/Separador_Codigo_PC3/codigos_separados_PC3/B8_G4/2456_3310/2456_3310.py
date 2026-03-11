#1 - 10%
#2-30%
#3 OU +40%

#LEIA: VALOR DA MENSALIDADE
#LEIA: NUMERO DE CRIANCAS

vm = float(input("Digite o valor da mensalidade: "))
nc = int(input("Digite o numero de criancas: "))

if(nc == 1) or (nc == 2) or (nc >=3):
	if(nc == 1):
		desc = vm * (10/100)
		vt = nc*(vm - desc)
	elif(nc == 2):
		desc = vm * (30/100)
		vt = nc*(vm - desc)
	elif(nc >= 3):
		desc = vm * (40/100)
		vt = nc*(vm - desc)
	print(round(vt,2))
#SAIDA: valor total da mesalidade COM desconto














