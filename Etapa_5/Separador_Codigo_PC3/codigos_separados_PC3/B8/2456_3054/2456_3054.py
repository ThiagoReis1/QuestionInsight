mensalidade = float(input("informe o valor: "))
crianca = int(input("informe as criancas: "))

if(crianca == 1):
	print(round(mensalidade-mensalidade*0.1, 2))
elif(crianca == 2):
	print(round(2*mensalidade-2*mensalidade*0.3, 2))
elif(crianca >= 3):
	print(round(3*mensalidade-3*mensalidade*0.4, 2))
	