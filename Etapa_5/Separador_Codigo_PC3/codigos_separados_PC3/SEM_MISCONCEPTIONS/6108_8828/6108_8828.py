qtd = float(input("quantidade de conbustivel comum:"))

if qtd < 17.5:
	total  = qtd +  1.5
	print(round(total, 2))
elif 17.5 < qtd <= 35:
	total = qtd +  2.3
	print(round(total, 2))
elif 35 < qtd <= 50:
	total = qtd + 3.3
	print(round(total,2))
else:
	total = qtd + 4.7
	print (round(total, 2))