X = int(input("digite um numero:"))

num_a = X // 1000

num_b = X % 1000

num_dif = ((num_a - num_b)**2)

if (X == num_dif):
	print(X, "atende a propriedade")
else:
	print(num_dif)
	