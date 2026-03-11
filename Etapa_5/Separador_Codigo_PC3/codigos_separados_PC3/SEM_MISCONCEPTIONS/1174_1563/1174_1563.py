N = int(input("Numero: "))
x = 1
y = 3
s = 0
v = ((-1*(x)**3/(9+y)) + (x+1)**3/(9+(y+2)))
if (N == 1):
	u = ((-1*(x)**3/(9+y)))
	s = (s + u)
	else:
		u = (v)
		s = (s + v)
	N = N+1
	x = x + 1
	y = y + 1
print (s)

