nome = input("machado ou lanca: ").lower()
fator = int(input("1-10: "))

if nome == 'machado':
	m = (30*fator)/10
	q = int(m)
	print(q)
else: 
	l = 5 + (20*fator)/10
	p = int(l)
	print(p)