n = int(input("Digite um numero inteiro x:"))

if(n%47 == 0):
	q = n//47
	print(q)
	print("sim")

else:
	r = n%47
	print(r)
	print("nao")