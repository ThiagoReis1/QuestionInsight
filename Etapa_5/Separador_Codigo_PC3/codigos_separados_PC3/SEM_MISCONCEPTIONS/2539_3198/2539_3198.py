v = float(input("valor do premio:"))
m = int(input("saque mensal:"))
j = float(input("juros:"))
a = (v * 0.2) + v

meses = 0
cont = 0
if(v< 0 or m < 0 or j < 0):
	print("Dados incorretos")
	
else:
	while (v < a):
		nv = ((v * j) + v) - m
		va = nv
		meses = meses + 1]
		print(round(meses , 2))

