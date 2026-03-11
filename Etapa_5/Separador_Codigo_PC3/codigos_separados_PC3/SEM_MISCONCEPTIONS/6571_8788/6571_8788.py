pac = float(input("peso do pacote em kg:"))

if pac < 5:
	taxa = 3.75
elif pac == 5:
	taxa = 4.75
else:
	taxa = 5.75
	
custo_fixo = 10
total = taxa + custo_fixo

print("total=",round(total,2))