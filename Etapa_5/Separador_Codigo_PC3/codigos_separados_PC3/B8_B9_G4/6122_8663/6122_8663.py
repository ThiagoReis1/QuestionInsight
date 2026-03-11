c = float(input())

if c < 17.5:
	s = 0.8
elif c >= 17.5 and c <35:
	s = 1.3
elif c >=35 and c < 50:
	s = 2.1
elif c > 50:
	s = 3
t = c + s
print(t)