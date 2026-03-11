x = int(input())
k = int(input())
ln = 1.0
i = 2
aux =-1
while(i>ln):
	ln = ln - ((x**i)/i + (x**i)/i - (x**i)/i + (x**i)/i)*aux
	i = i + 1
	aux = aux*(-1)
	print(round(ln,10))
