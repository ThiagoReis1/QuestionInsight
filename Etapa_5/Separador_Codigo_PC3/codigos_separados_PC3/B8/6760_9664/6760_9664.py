# faça seu código aqui!
qp= int(input("quantidade de pecas: "))

if qp<10:
	custo= (30+3.25)
	print(round(custo,2))
elif qp==10:
	custo=(30+4.50)
	print(round(custo,2))
elif qp>10:
	custo= (30+6)
	print(round(custo,2))