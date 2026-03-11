s = float(input())
d = float(input())
m = float(input())
j = float(input())
sm = d
t = 0
if (s > 0 and d > 0 and m > 0 and j > 0):
	while (sm <= s):
		sm = sm + m - (sm * j)
		t = t + 1
	print(t)
else:
	print("Dados incorretos")