num = int(input("insira um numero: "))
p1 = num // 100
p2 = num % 100
x = (p1 + p2)**2
print(num)
if (num == x):
	print("atende")
else:
	print("nao atende")