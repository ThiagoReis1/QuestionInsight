p = int(input("p: "))
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
n = n1 + n2 + n3
t = 10*n

if((p - t) > 0):
	print(p-t)
	print("Vivo".upper())
else:
	print("0")
	print("Morto".upper())