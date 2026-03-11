num = int(input("digite um numero: "))
p1 = num // 1000
p2 = num % 1000
x = ((p1)-(p2))**4
if (num ==x) :
	print(num)
	print("atende")
else:
	print(num)
	print("nao atende")