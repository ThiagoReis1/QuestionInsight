c = float(input("Digite a quantidade de combustivel comum: "))
if(c < 17.5):
	total = c + 0.8
	print(total)
elif((c >= 17.5) and (c < 35)):
	total = c + 1.3
	print(total)
elif((c >= 35) and (c < 50)):
	total = c + 2.1
	print(total)
else:
	total = c + 3
	print(total)