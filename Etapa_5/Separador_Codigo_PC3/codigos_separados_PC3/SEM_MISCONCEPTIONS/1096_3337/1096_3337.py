num = int(input())

primeiros = num // 10000
segundos = (num % 10000) // 100
terceiros = (num % 10000) % 100

if ( primeiros**3 + segundos**3 + terceiros**3 == num ):
	print("atende")
else:
	print("nao atende")
print(num)	