comb = float(input("Quantidade de combustivel comum: "))

if (comb < 17.5):
	total = comb + 1.5
elif (comb >= 17.5 and comb < 35):
	total = comb + 2.3
elif (comb >= 35 and comb < 50):
	total = comb + 3.3
else:
	total = comb + 4.7
print(total)