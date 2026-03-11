qb = int(input("qtd de batatas: "))

if qb < 10:
	b=0.90
	t= b * qb
	
else:
	b= 0.75
	t= qb * b
print(round(t,2))
	