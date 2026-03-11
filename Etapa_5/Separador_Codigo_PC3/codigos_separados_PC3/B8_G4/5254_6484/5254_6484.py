preco = float(input())
cod = int(input())

n1 = 1
n2 = 2
n3 = 3
n4 = 4

if cod == n1:
	total = (preco - (preco*0.40)) + preco*(0.10)
	print(round(total,2))
elif cod == n2:
	total = (preco - (preco*0.40)) + preco*(0.08)
	print(round(total,2))
elif cod == n3:
	total = (preco - (preco*0.40)) + preco*(0)
	print(round(total,2))
elif cod == n4:
	total = (preco -(preco*0.40)) + preco*(0.02)
	print(round(total,2))