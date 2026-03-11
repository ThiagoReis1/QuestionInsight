x = int(input("Entre com a variavel x: "))

if x % 31 == 0:
	q = x // 31
	print(q)
	print("sim")
else:
	r = x % 31 
	print(r)
	print("nao")