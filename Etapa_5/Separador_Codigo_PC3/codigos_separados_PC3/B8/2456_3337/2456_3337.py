mensalidade = float(input())
criancas = int(input())

if criancas == 1:
	mensal = mensalidade - (mensalidade*10)/100
	print(round(criancas*mensal,2))	
elif criancas == 2:
	mensal = mensalidade - (mensalidade*30)/100
	print(round(criancas*mensal,2))	
elif criancas >= 3:
	mensal = mensalidade - (mensalidade*40)/100
	print(round(criancas*mensal,2))	

	