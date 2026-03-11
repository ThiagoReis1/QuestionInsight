num = int(input())
n=num
p3 = n%100
n=n//100
p2 = n%100
n=n//100
p1 = n

calculo = p1**3 + p2**3 + p3**3

if(num==calculo):
	print("atende")
	print(num)
else:
	print("nao atende")
	print(num)