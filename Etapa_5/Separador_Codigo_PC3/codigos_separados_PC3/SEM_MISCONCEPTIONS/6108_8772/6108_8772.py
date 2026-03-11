comb = float(input())

if comb< 17.5:
	qtde = 1.5
elif 17.5 <= comb < 35:
	qtde = 2.3
elif 35 <= comb < 50:
	qtde = 3.3
else:
	qtde = 4.7
	
total = comb + qtde
print(round(total,1))