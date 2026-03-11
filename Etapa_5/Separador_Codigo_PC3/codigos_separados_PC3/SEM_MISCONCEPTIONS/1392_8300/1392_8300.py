consumo= float(input("Digite o consumo em m: "))
taxa_base = 30.00
if consumo <10:
		taxa_m3= 3.00
else:
		taxa_m3= 3.50
valor_conta= taxa_base + consumo * taxa_m3
print(round(valor_conta,2))



	

