N = int(input())

np = 0
nd = 0

while (N != 0):
		nd = nd + 1
		if (N > 0):
			np = np + 1

		N = int(input())
print(nd)
print((round(((np/nd)*100),2)))

