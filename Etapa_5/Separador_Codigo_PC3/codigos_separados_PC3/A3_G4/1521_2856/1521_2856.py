n = int(input("n: "))
e = int(input("e: "))
q = int(input("q: "))
x = e
y = 0
while (x > 0):
	v = x - n + y*q
	x = e - n
	y = y + 1
print(y)