num = int(input("digite o numero:"))
p1 = num // 10000
p2 = num %10000
x = (p1 + p2)**2
print(num)
if (x == num):
	print("atende")
else:
	print("nao atende")