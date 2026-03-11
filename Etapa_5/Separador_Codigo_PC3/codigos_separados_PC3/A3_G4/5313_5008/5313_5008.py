x = float(input("bogomips: "))
k = 0
cont = 0
x1 = 0
while (k <= 7206.14):
	k = 0.65*x
	print(k)
	x += k
	cont += 1
	print(cont)
print(cont)