x = float(input())
k = int(input())

a = 1
b = 0
ex = 1
c = 0
f = 0

while(b<k and x>-1 and x<1 and k!=0):
	f = (x**ex)/a
	c = c + f
	ex = ex + 2
	a = a + 2
	b = b + 1
print(round(c, 7))