x = input()
q = int(input())
s = int(input())

if x == 'C':
	preco = q*2 + s*6
	print(round(preco,2))
else:
	preco = q*4.50 + s*6
	print(round(preco,2))
	