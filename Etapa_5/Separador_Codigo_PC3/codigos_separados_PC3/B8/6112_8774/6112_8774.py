comb= float(input("digite a qtde de combustivel: "))

if comb < 17.5:
	total= comb + 10.5
	print(total)
elif comb > 17.5 and comb <= 35:
	total= comb + 14
	print(total)
elif comb > 35 and comb <= 50:
	total= comb + 18.6
	print(total)
elif comb >= 50:
	total= comb + 24.5
	print(total)