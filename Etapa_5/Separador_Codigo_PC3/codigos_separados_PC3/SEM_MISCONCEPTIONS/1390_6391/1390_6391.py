consumo_do_Plano = float(input("Determine o valor consumido pelo cliente: "))

tarifa_min = 1.20
taxa_fixa = 25.00 + consumo_do_Plano * 1.40

if (consumo_do_Plano <= 100):
	Valor_da_conta = tarifa_min * consumo_do_Plano
else :
	Valor_da_conta = taxa_fixa
	
print(round(Valor_da_conta, 2))