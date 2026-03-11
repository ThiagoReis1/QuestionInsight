di = float(input())
nap = int(input())

tx = 0.012
mes = 0

while (mes < nap):
	di = di + di*tx
	
	mes = mes + 1
	
	print(round(di,2))
	

