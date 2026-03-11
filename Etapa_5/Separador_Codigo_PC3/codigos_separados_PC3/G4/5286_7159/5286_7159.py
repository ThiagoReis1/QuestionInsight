N = int(input())

nd = 0
nm = 0

while(N != 0 and N > 0):
		nd = nd + 1
		if(N % 2 == 0):
			nm = nm + 1
		N = int(input())
print(nd)
print(round((nm/nd) * 100, 2))