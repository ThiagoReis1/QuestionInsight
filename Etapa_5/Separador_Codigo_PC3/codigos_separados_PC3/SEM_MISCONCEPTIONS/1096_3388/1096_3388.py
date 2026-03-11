num = int(input())
n1 = num // 10000
resto_n1 = num % 10000
n2 = resto_n1 // 100
resto_n2 = resto_n1 % 100
if ((n1 ** 3) + (n2 ** 3) + (resto_n2 ** 3)) == num:
	print("atende")
else:
	print("nao atende")
print(num)
	