x = int(input("qual o valor de x? "))
y = 31
x1 = x % y
x2 = x // y
if (x1 == 0):
	print(x2)
	print("sim")
else:
	print(x1)
	print("nao")