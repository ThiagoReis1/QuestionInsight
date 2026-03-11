n = int(input())
m = input().upper()
if n <= 2002 and m=="B":
	print("sim")
	g = 2002 - n
	print(g)
elif n>2002 and m=="B":
	print("nao")
	z = n - 2002
	print(z)
elif n<=2003 and m=="J":
	print("sim")
	f = 2003 - n
	print(f)
elif n>2003 and m=="J":
	print("nao")
	x = n - 2003
	print(x)
