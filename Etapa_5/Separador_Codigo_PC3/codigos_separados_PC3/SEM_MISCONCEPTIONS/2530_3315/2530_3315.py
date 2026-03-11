d=float(input())
tf=float(input())
j=float(input())

saldo = d
meses = 0
x = 1.15*d

if(d>0 and tf>0 and j>0):
	while(saldo <= x):
		saldo = saldo + (j/100)*saldo
		saldo = round(saldo,2)
		saldo = saldo-tf
		meses = meses + 1
	print(meses)
else:
	print("Dados incorretos")