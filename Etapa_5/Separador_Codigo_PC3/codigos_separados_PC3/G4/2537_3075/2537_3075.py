v = float(input())
m = float(input())
j = float(input())
s = v
t = 1

if (v < 0 or m < 0 or j < 0):
	print("Dados incorretos")
else:
	while(s <= (v + v*0.2)):
		s = (s - m) + s*(j*t)
		t = t + 1
	print(t)