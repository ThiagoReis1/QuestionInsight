concessionaria=float(input("digite o consumo= "))


if concessionaria <10^3:
	total= (concessionaria * 3 ) + 30
	print(round(total,2))
if concessionaria >= 10^3:
	total= (concessionaria * 3.5) + 30
	print(round(total,2))
	