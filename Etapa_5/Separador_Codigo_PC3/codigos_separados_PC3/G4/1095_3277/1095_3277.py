n=int(input("numero: "))
d1= (n // 10000) %10000
d2= n % 10000
print(d1)
print(d2)
if((d1 + d2)** 2 == n):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")