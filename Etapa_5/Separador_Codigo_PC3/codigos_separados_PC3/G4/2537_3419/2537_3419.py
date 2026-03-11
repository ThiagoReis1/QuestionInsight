v = float(input("valor do preco"))
m = float(input("saque fixo"))
i = float(input("taxa de jurs"))

j = i/100
s = v
meses = 0

if (v>0) and (m>0) and (j>0):
	while(s <= 1.20*v):
		s = s + (s*j)
		s = s - m
		s = round(s,2)
		meses = meses + 1 
	print(meses)
else:
	print("Dados incorretos")
	

