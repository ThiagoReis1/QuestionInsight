x = float(input("Valor de x: "))
k = int(input("Numero de series: "))

cont = 0
ac = 0

if(x < 1 and x > -1):
	while(k > cont):
		ac = ac + ((-1) ** cont) * (x**cont)
		cont = cont + 1
	print(round(ac,7))