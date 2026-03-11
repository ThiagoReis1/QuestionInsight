conta = float(input("insira o valor da conta"))
gorjeta300 = conta + conta * 10 /100
gorjeta301 = conta + conta * 6 / 100
if(conta <= 300):
	print(round(gorjeta300,2))
else:
	print(round(gorjeta301,2))