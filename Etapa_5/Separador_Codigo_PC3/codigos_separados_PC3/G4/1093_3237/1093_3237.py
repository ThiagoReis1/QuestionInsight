x = int(input())
a = x//100
b = x%100

k = a**2 + b**2
if x == k:
	print("atende")
else:
	print("nao atende")
	
print(x)