v = float(input("valor do premio:"))
m = float(input("saque mensal:"))
j =  float(input("taxa de juros:"))

s = v
j = i/100
meses = 0 

if (v>0) and ( m>0) and (j>0):
	while (s <= 1.20 *v):
	s = (s - m)
	s = s + (s*j)
	s  = round(s,2)
	meses = meses + 1
	print(meses)
	
else:	
	
	print("Dados incorretos")
