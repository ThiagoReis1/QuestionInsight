qp = int(input("insira a quantidade de pecas de roupa: "))

taxa = 30.0

if qp == 10:
	total = taxa + 4.5
	print("total= ", round(total, 2))
elif qp < 10:
	total = taxa + 3.25
	print("total= ", round(total, 2))
else:
	total = taxa + 6.0
	print("total= ", round(total, 2))
	
