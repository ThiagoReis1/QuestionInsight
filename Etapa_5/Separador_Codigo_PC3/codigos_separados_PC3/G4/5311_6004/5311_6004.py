d = float(input("deposito inicial: "))
m = int(input("numero de meses de aplicacao: "))


while(d <= 0):
	d = (d*0.012)+m

print(round(d, 2))
