quantcombustivel = float(input("Digite a quantidade de combustivel comum: "))

if quantcombustivel<17.5:
	total = quantcombustivel+1.5
elif quantcombustivel>=17.5 and quantcombustivel<35:
	total = quantcombustivel+2.3
elif quantcombustivel>=25 and quantcombustivel<50:
	total = quantcombustivel+3.3
else:
	total = quantcombustivel+4.7
print(round(total,1))