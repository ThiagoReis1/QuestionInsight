x = float(input(""))
k = int(input(""))
t = 0
y = 1
u = 0
p = 0
while(t != k):
	p = p+ y*(x**u)
	u = u + 2
	t = t + 1
	y = y *(-1)
print(round(p, 8))