qi = int(input())
qc = int(input())
pi = float(input())
pc = float(input())

t = 0 
i = qi 
c = qc

while(i+c <= 50000):
	i = i + i*(pi/100)
	c = c + c*(pc/100)
	t = t + 1
print(t)	