# faça seu código aqui!
ME = int(input())

if ME < 4:
	x = 20. * ME
	print(round(x, 2))

else:
	T = ME * 20.
	D = T * (15/100)
	y = T - D
	print(round(y, 2))