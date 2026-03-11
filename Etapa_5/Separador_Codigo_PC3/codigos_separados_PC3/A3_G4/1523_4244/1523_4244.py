F = 200
i = int(input())
c = int(input())
d = int(input())

t = 0
p = 0
while(F > p+i):
	s = p + c - d
	p = c - d + p
	t = t + 1
print(t)
