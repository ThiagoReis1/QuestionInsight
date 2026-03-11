from numpy import *
n = float(input("s"))
x= array(eval(input("a")))
y= array(eval(input("b")))
q = n / (n - 1)
n = 0
i = 0
v = x + y
while i < size(v):
	n = abs(v[i]) ** q + n
	i = i + 1
n = n ** (1 / q)
print(round(n, 5))