vendas = float(input("volume de vendas: "))

if vendas <= 1000 :
	cota = vendas*0.05

else:
	cota = 1000*0.05+(vendas-1000)*0.1
	
print(round(cota,2))