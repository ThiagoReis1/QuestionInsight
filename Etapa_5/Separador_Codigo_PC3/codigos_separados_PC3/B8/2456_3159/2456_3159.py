valor_mensalidade = float(input("Informe o valor da mensalidade :"))
num_crianca = int(input("Informe o numero de criancas :"))

if (num_crianca == 1):
	valor_total = (valor_mensalidade * num_crianca)
	valor_tot = (valor_mensalidade + valor_total)*10//100
	print(valor_tot)

elif(num_crianca == 2):
	valor_total =  valor_mensalidade*num_crianca
	valor_tot = (valor_mensalidade + valor_total)*30//100
	print(valor_tot)

elif(num_crianca >=3):
	valor_total = (valor_mensalidade * num_crianca)*40//100
	valor_tot = (valor_mensalidade + valor_total)
	print(valor_tot)
