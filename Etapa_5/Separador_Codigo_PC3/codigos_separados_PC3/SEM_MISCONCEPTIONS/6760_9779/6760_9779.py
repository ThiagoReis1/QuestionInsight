roupas=float(input("roupas:"))

if (roupas<10):
	custo=30+3.25
	print(round(custo,2))
elif (roupas==10):
	custo=30+4.50
	print(round(custo,2))
else:
	custo=30+6
	print(round(custo,2))
	