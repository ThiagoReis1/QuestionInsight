from math import*
x=float(input("numeron real:"))
k=int(input("numero inteiro"))
m=1
y=1
senh = 0
while (m <= k):
	senh= senh + (x**y)/factorial(y)
	m=m+1
	y=y+2
print(round(senh,9))