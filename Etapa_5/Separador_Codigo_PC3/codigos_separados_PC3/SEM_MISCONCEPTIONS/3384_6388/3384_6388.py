unidade=input(" O para oncas, ou K para kilograms: ").upper()
valor_med=float(input("valor da medida? "))


conver=35.274*valor_med
conver1=valor_med/35.274

if unidade=="K":
	conversao=conver
else:
	conversao=conver1
	
print(round(conversao,2))
