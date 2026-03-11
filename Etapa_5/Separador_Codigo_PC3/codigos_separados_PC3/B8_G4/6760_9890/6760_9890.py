# faça seu código aqui!
q=int(input("Quantidade de pecas de roupa: "))

if q < 10:
	t=3.25 + 30
	print(round(t,2))
elif q == 10:
	t=4.50+30
	print(round(t,2))
elif q > 10:
	t=6+30
	print(round(t,2))