conta = float(input("valor da conta "))

if(conta <= 300.0):
	contaf = (conta/100) * 10 + conta
	print(round(contaf, 2))
else:
	contaf = (conta/100) * 6 + conta
	print(round(contaf, 2))