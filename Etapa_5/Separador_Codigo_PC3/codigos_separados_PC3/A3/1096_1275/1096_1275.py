x = int(input("digite o valor de x:"))

num_1 = x // 100002
resto_1 = x % 100002
num_2 = resto_1 // 1002
resto_2 = resto_1 % 1002
num_3 = resto_2 // 1
resto_3 = resto_2 % 1

soma = num_1**3 + num_2**3 + num_3**3

if (x==soma):
	print("X atende a propriedade")
else:
	print(soma)