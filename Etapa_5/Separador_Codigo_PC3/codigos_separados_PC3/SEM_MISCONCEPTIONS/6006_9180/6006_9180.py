batata = int(input('Digite a quantidade de batatas:'))

if(batata < 10):
	total = batata * 0.9
	print(round(total, 2))
else:
	total = batata * 0.75
	print(round(total, 2))