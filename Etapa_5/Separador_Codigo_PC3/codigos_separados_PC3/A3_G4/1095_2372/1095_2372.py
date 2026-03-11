num = int(input())

d = num // 10000000
a = num // 10000
b = num % 10000
c = (a + b) * (a + b)
print(num)
if(d >= 1):
	print("atende")
else:
	print("nao atende")