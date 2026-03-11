x = int(input("digite um numero: "))
k = 0
contk = 0
l = 0
contl = 0
while(x != 0):
	if (x % 2 == 0):
		k = k + x
		contk = contk + 1
	else:
		l = l + x
		contl = contl + 1
	x = int(input("digite um numero: "))
print (round(k / contk , 2))
print (round(l / contl , 2))
		