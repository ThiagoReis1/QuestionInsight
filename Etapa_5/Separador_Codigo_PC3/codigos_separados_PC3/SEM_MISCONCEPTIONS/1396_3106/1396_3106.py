conta = float(input("Valor da conta: "))

if (conta <= 300):
	final = conta * 1.1

else:
	final = conta*1.06
	
print(round(final,2))