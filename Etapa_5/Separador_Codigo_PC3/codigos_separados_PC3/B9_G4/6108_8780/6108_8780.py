comb = float(input("Digite a qtde. de combustivel comum: "))

if comb < 17.5:
	coax = comb + 1.5
elif comb >= 17.5 and comb < 35:
	coax =  comb + 2.3
elif comb >= 35 and comb < 50:
	coax = comb + 3.3
else:
	coax = comb + 4.7
	
print(coax)