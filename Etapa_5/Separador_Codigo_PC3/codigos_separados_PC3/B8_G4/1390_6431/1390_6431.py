x = float(input("Digite a quantidade de minutos: "))

if x <= 100:
	t = x * 1.20
	
	print(round(t,2))
	
elif x >= 101:
	i = 25 + (1.40 * x)
	print(round(i,2))