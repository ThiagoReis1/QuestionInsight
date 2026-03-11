d = int(input("Digite a distancia em km: "))
ci = 50.00

if (d < 10):
	total = ci + 5.5
elif (d == 10):
	total = ci + 7.75
elif (d > 10):
	total = ci + 10
print(total)