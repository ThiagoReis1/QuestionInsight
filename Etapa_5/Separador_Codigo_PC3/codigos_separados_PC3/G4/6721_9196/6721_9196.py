x = int(input("numero:"))
y = x % 13
z = x // 13

if y == 0:
	print(z)
	print ("sim")

else:
	print(y)
	print ("nao")